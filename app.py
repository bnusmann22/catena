"""
Catena — USSD data capture for farmers (Africa's Talking sandbox)

Run:
    pip install flask africastalking python-dotenv
    python app.py
Then: ngrok http 5000  ->  paste the https URL + "/ussd" into
the AT dashboard's USSD channel callback field.
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
if AT_API_KEY:
    import africastalking
    africastalking.initialize(AT_USERNAME, AT_API_KEY)
    sms = africastalking.SMS

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


@app.route("/", methods=["GET"])
def index():
    return (
        "Catena USSD Service is active!<br>"
        "USSD Webhook Callback URL: <code>/ussd</code> (POST)<br>"
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

            response = f"END Logged: {qty_val}kg {produce}. Confirmation SMS sent."
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