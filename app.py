"""
Catena — USSD & Voice data capture for farmers (Africa's Talking sandbox)

Run:
    pip install flask africastalking python-dotenv
    python app.py
Then: ngrok http 5000  ->  paste the https URL + "/ussd" into the AT
dashboard's USSD callback, and the URL + "/voice" into the Voice callback.
"""

import os
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()  # reads .env into os.environ

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Africa's Talking setup (SMS). Safe to leave creds unset while you're just
# testing the menu tree — SMS calls are wrapped in try/except below.
# ---------------------------------------------------------------------------
AT_USERNAME = os.environ.get("AT_USERNAME", "sandbox")
AT_API_KEY = os.environ.get("AT_API_KEY", "")

sms = None
voice = None
if AT_API_KEY:
    import africastalking
    africastalking.initialize(AT_USERNAME, AT_API_KEY)
    sms = africastalking.SMS
    voice = africastalking.Voice

# ---------------------------------------------------------------------------
# "Database" — in-memory. Pre-load a couple of fake farmers so the demo
# doesn't open on an empty state.
# ---------------------------------------------------------------------------
suppliers = {
    "+2348012345678": {"name": "Musa Ibrahim", "produce": "Cassava"},
    "+2348023456789": {"name": "Amina Yusuf", "produce": "Maize"},
}

harvest_reports = [
    {"phone": "+2348012345678", "produce": "Cassava", "qty_kg": 50, "ts": "2026-08-27 09:14"},
    {"phone": "+2348023456789", "produce": "Maize", "qty_kg": 120, "ts": "2026-08-28 07:02"},
]

# Dummy prices for option 3
PRICES = {
    "cassava": 180,
    "maize": 250,
    "yam": 400,
    "rice": 700,
}


def send_sms(phone: str, message: str):
    """Fire-and-forget SMS confirmation. Never let this break the USSD flow."""
    if not sms:
        print(f"[SMS DISABLED — would send to {phone}]: {message}")
        return
    try:
        sms.send(message, [phone])
    except Exception as e:
        print(f"[SMS ERROR] {e}")


def _voice_xml(body: str):
    """Return a properly formatted Africa's Talking Voice API XML response."""
    xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<Response>\n{body}\n</Response>'
    return xml, 200, {"Content-Type": "application/xml"}


def make_confirmation_call(phone: str, produce: str, qty_kg: int):
    """Make an outbound voice call to confirm a harvest was logged.
    Requires AT_PHONE_NUMBER (your Africa's Talking virtual number)."""
    caller_id = os.environ.get("AT_PHONE_NUMBER", "")
    if not voice or not caller_id:
        print(f"[VOICE DISABLED — would call {phone}]: Harvest confirmed: {qty_kg}kg {produce}")
        return
    try:
        voice.call(caller_id, [phone])
        print(f"[VOICE CALL] Confirmation call initiated to {phone}")
    except Exception as e:
        print(f"[VOICE ERROR] {e}")


@app.route("/", methods=["GET"])
def index():
    return (
        "Catena USSD & Voice Service is active!<br>"
        "USSD Webhook Callback URL: <code>/ussd</code> (POST)<br>"
        "Voice Webhook Callback URL: <code>/voice</code> (POST)<br>"
        "Debug State URL: <a href='/debug/state'>/debug/state</a> (GET)",
        200,
    )


@app.route("/ussd", methods=["GET", "POST"])
def ussd():
    session_id = request.values.get("sessionId", "")
    phone = request.values.get("phoneNumber", "")
    text = request.values.get("text", "")

    parts = text.split("*") if text else []
    response = ""

    # If accessed directly via GET in a browser with no params, show helpful indicator
    if request.method == "GET" and not request.values:
        return (
            "CON Welcome to Catena USSD Endpoint\n"
            "(Active - Ready to receive POST requests from Africa's Talking)",
            200,
            {"Content-Type": "text/plain"},
        )

    # ---- Root menu ---------------------------------------------------
    if text == "":
        response = (
            "CON Welcome to Catena\n"
            "1. Register as supplier\n"
            "2. Report harvest\n"
            "3. Check today's price"
        )

    # ---- Option 1: Register as supplier -------------------------------
    elif parts[0] == "1":
        if len(parts) == 1:
            response = "CON Enter your name"
        elif len(parts) == 2:
            response = "CON Enter your produce type (e.g. Cassava)"
        elif len(parts) == 3:
            name = parts[1]
            produce = parts[2]
            suppliers[phone] = {"name": name, "produce": produce}
            response = f"END Registered! Welcome, {name}. Produce: {produce}."
        else:
            response = "END Invalid input."

    # ---- Option 2: Report harvest --------------------------------------
    elif parts[0] == "2":
        if len(parts) == 1:
            response = "CON Enter produce type"
        elif len(parts) == 2:
            response = "CON Enter quantity in kg"
        elif len(parts) == 3:
            produce = parts[1]
            qty = parts[2]
            try:
                qty_val = int(qty)
            except ValueError:
                response = "END Invalid quantity. Please restart and enter a number."
                return _reply(response)

            from datetime import datetime
            record = {
                "phone": phone,
                "produce": produce,
                "qty_kg": qty_val,
                "ts": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
            harvest_reports.append(record)
            print(f"[HARVEST LOGGED] {record}")

            send_sms(
                phone,
                f"Harvest logged: {qty_val}kg {produce}. You'll be notified when picked up.",
            )
            make_confirmation_call(phone, produce, qty_val)

            response = f"END Logged: {qty_val}kg {produce}. Confirmation sent."
        else:
            response = "END Invalid input."

    # ---- Option 3: Check today's price ---------------------------------
    elif parts[0] == "3":
        if len(parts) == 1:
            options = "\n".join(f"{i+1}. {p.title()}" for i, p in enumerate(PRICES))
            response = f"CON Select produce:\n{options}"
        elif len(parts) == 2:
            keys = list(PRICES.keys())
            try:
                idx = int(parts[1]) - 1
                produce = keys[idx]
                response = f"END {produce.title()}: \u20a6{PRICES[produce]}/kg today"
            except (ValueError, IndexError):
                response = "END Invalid selection."
        else:
            response = "END Invalid input."

    else:
        response = "END Invalid option."

    return _reply(response)


def _reply(response: str):
    return response, 200, {"Content-Type": "text/plain"}


# ---------------------------------------------------------------------------
# Voice API endpoints  (set callback URL to <ngrok>/voice in AT dashboard)
# ---------------------------------------------------------------------------

@app.route("/voice", methods=["POST"])
def voice_callback():
    """Main voice callback — handles inbound IVR calls and outbound confirmations."""
    is_active = request.values.get("isActive")
    direction = request.values.get("direction", "")

    # Call ended
    if is_active == "0":
        return _voice_xml("")

    # --- Outbound call: harvest confirmation callback ---
    if direction == "Outbound":
        phone = request.values.get("destinationNumber", "")
        caller_harvests = [r for r in harvest_reports if r["phone"] == phone]
        if caller_harvests:
            latest = caller_harvests[-1]
            return _voice_xml(
                f'<Say>Hello, this is Catena. '
                f'Your harvest of {latest["qty_kg"]} kilograms of {latest["produce"]} '
                f'has been successfully recorded. '
                f'You will be notified when pickup is scheduled. '
                f'Thank you. Goodbye.</Say>'
            )
        return _voice_xml(
            '<Say>Hello, this is Catena. '
            'Your harvest has been recorded. Thank you. Goodbye.</Say>'
        )

    # --- Inbound call: IVR price query + harvest status ---
    base = request.url_root.rstrip("/")
    return _voice_xml(
        f'<GetDigits timeout="30" finishOnKey="#" callbackUrl="{base}/voice/menu" numDigits="1">'
        '<Say>Welcome to Catena Agricultural Services. '
        'Press 1 to check commodity prices. '
        'Press 2 to hear your latest harvest report. '
        'Press hash when done.</Say>'
        '</GetDigits>'
        '<Say>We did not receive your input. Goodbye.</Say>'
    )


@app.route("/voice/menu", methods=["POST"])
def voice_menu():
    """Route the caller based on their main-menu DTMF selection."""
    digits = request.values.get("dtmfDigits", "")
    base = request.url_root.rstrip("/")

    # --- Option 1: commodity price list ---
    if digits == "1":
        items = " ".join(
            f"Press {i + 1} for {p.title()}." for i, p in enumerate(PRICES)
        )
        return _voice_xml(
            f'<GetDigits timeout="30" finishOnKey="#" callbackUrl="{base}/voice/price-result" numDigits="1">'
            f'<Say>{items}</Say>'
            '</GetDigits>'
            '<Say>No input received. Goodbye.</Say>'
        )

    # --- Option 2: latest harvest report ---
    if digits == "2":
        phone = request.values.get("callerNumber", "")
        caller_harvests = [r for r in harvest_reports if r["phone"] == phone]
        if caller_harvests:
            latest = caller_harvests[-1]
            return _voice_xml(
                f'<Say>Your latest harvest report is '
                f'{latest["qty_kg"]} kilograms of {latest["produce"]}, '
                f'logged on {latest["ts"]}. '
                f'Thank you for using Catena. Goodbye.</Say>'
            )
        return _voice_xml(
            '<Say>No harvest reports found for your number. '
            'Please log a harvest via U S S D first. Goodbye.</Say>'
        )

    return _voice_xml('<Say>Invalid selection. Goodbye.</Say>')


@app.route("/voice/price-result", methods=["POST"])
def voice_price_result():
    """Read back the selected commodity price via voice."""
    digits = request.values.get("dtmfDigits", "")
    keys = list(PRICES.keys())

    try:
        idx = int(digits) - 1
        if idx < 0:
            raise IndexError
        produce = keys[idx]
        price = PRICES[produce]
        return _voice_xml(
            f'<Say>{produce.title()} is currently {price} Naira per kilogram. '
            f'Thank you for using Catena. Goodbye.</Say>'
        )
    except (ValueError, IndexError):
        return _voice_xml('<Say>Invalid selection. Goodbye.</Say>')


@app.route("/debug/state", methods=["GET"])
def debug_state():
    """Not for the demo audience — quick way to eyeball state from a browser
    or curl while you're building."""
    lines = ["-- Suppliers --"]
    for phone, info in suppliers.items():
        lines.append(f"{phone}: {info}")
    lines.append("\n-- Harvest Reports --")
    for r in harvest_reports:
        lines.append(str(r))
    return "\n".join(lines), 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)