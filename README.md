# Catena — Empowering Smallholder Agriculture via Last-Mile Telecom

**Catena** is a last-mile agricultural supply chain and data aggregation platform built to connect rural smallholder farmers directly to modern agro-dealers, food processors, and logistics networks. By leveraging ubiquitous telecom channels—**USSD** and **Automated Voice (IVR)**—Catena operates entirely without the need for smartphones, mobile data, or internet connectivity.

---

## 🌍 The Problem Catena Solves

In emerging agricultural economies, smallholder farmers produce over **70–80% of domestic food supplies**, yet remain structurally isolated from formal markets:

1. **The Digital Divide & Device Barrier**: Most rural farmers own basic 2G/3G feature phones ("dumbphones") and live in areas with unreliable internet coverage. Smartphone-based mobile apps fail to penetrate these communities.
2. **Information Asymmetry & Middlemen Exploitation**: Without direct access to live wholesale commodity pricing, farmers are forced to accept predatory, below-market rates offered by unregulated middlemen at the farm gate.
3. **Severe Post-Harvest Food Loss**: Up to 40% of fresh produce spoils in fields due to lack of visibility. Aggregators and logistics providers cannot plan truck dispatch schedules until produce is already rotting because they have no advance notice of harvest readiness.
4. **Lack of Transaction Records & Financial Exclusion**: Because farming deals are conducted verbally or on scrap paper, smallholders have no verifiable transaction history or production track record, making it nearly impossible to access micro-loans, insurance, or input subsidies.
5. **Literacy & Language Constraints**: Text-heavy applications and written documents exclude farmers with low literacy levels or those who communicate primarily via spoken native languages.

Catena removes these structural bottlenecks by turning **any basic mobile phone** into a secure, real-time supply chain terminal.

---

## 💼 Core Business Value & Strategic Impact

Catena delivers tangible economic value across the entire agricultural value chain:

```
┌────────────────────────────────────────────────────────┐
│                   RURAL FARM GATE                      │
│   Basic Feature Phone (No Internet / No Smartphone)   │
└───────────────────────────┬────────────────────────────┘
                            │ USSD (*384*1#) / Voice (IVR)
                            ▼
┌────────────────────────────────────────────────────────┐
│                        CATENA                          │
│     Real-Time Data Capture & Verification Engine       │
└─────────────┬────────────────────────────┬─────────────┘
              │ Instant SMS Receipt        │ Real-Time Pipeline
              ▼                            ▼
┌───────────────────────────┐  ┌─────────────────────────┐
│     FARMER EMPOWERMENT    │  │  OFF-TAKERS & LOGISTICS │
│ • Fair Market Pricing     │  │ • Yield Forecasting     │
│ • Production Audit Trail  │  │ • Fleet Route Planning  │
│ • Zero Data Cost          │  │ • Reduced Spoilage      │
└───────────────────────────┘  └─────────────────────────┘
```

- **Zero-Barrier Digital Inclusion**: Operates over GSM telecom signaling channels. Farmers incur zero data costs, do not need to download an application, and do not need to create complex account passwords.
- **Predictive Aggregation & Supply Visibility**: Commercial buyers, cooperatives, and food manufacturers gain instant, day-by-day visibility into available harvest quantities across rural clusters before produce leaves the farm.
- **Optimized Logistics & Reduced Food Spoilage**: Logistics managers can consolidate transport routes, dispatch refrigerated trucks, and allocate warehouse space dynamically based on confirmed harvest volumes.
- **Financial Empowerment & Trust**: Farmers receive immediate digital confirmation receipts for every transaction, eliminating billing disputes and laying the groundwork for digital credit scoring.

---

## 🌟 Features & Business Importance

Each feature in Catena is intentionally designed to address a critical friction point in agricultural commerce:

### 1. Farmer & Supplier Onboarding (`*384*1#` ➔ Option 1)
- **What It Does**: Enables farmers to self-register their identity and primary crop (e.g., Cassava, Maize, Yam, Rice) in seconds using their phone number as a unique identifier.
- **Why It Matters for Business**:
  - Automatically transforms an informal, scattered farmer base into a structured, geolocated supplier registry.
  - Enables cooperatives and enterprise buyers to track supplier capacity, plan procurement campaigns, and meet international traceability and ESG standards.

### 2. Real-Time Harvest Reporting (`*384*1#` ➔ Option 2)
- **What It Does**: Allows farmers to instantly report harvested crop types and volume (in kilograms) as soon as crops are pulled from the field.
- **Why It Matters for Business**:
  - Provides FMCGs and food processors with immediate lead time to arrange pickups before perishable crops degrade.
  - Replaces slow, manual, paper-based field surveys with instant digital reporting, cutting aggregation turnaround times from days to hours.

### 3. Automated SMS Receipts & Production Audit Trails
- **What It Does**: Triggers an instantaneous, automated SMS receipt directly to the farmer’s handset upon logging a harvest (e.g., *"Harvest logged: 120kg Maize. You'll be notified when picked up."*).
- **Why It Matters for Business**:
  - **Eliminates Disputes**: Creates a verifiable, shared record between field agents, aggregators, and farmers, preventing weight disputes or under-reporting.
  - **Unlocks Rural Credit**: Serves as verifiable proof-of-production that microfinance institutions and agricultural banks can use to underwrite seasonal loans and crop insurance.

### 4. Automated Voice Confirmation Calls & Inbound IVR Services
- **What It Does**: Catena features an integrated telecom voice engine:
  - **Outbound Confirmation**: Automatically calls the farmer after a harvest is logged, speaking the confirmation aloud.
  - **Inbound IVR Hotline**: Farmers can dial in to listen to market prices or have their latest harvest submission read back to them.
- **Why It Matters for Business**:
  - **Overcomes Illiteracy**: Enables farmers who cannot read or write to interact fully with the platform through spoken voice.
  - **Builds High Trust**: Receiving an automated, official phone call reassures farmers that their produce has been recognized and prioritized for collection.

### 5. Transparent Daily Market Price Discovery (`*384*1#` ➔ Option 3)
- **What It Does**: Provides on-demand lookups of official daily wholesale benchmark prices (e.g., Cassava, Maize, Yam, Rice in ₦/kg).
- **Why It Matters for Business**:
  - **Eradicates Predatory Pricing**: Farmers gain bargaining power against exploitative middlemen by knowing prevailing market rates.
  - **Stabilizes Commodity Supply**: Encourages farmers to sell through legitimate cooperative channels that honor benchmark rates, ensuring stable supply chains for processors.

### 6. Live Supply Chain Inspection & Monitoring API
- **What It Does**: Provides a lightweight inspection endpoint (`/debug/state`) exposing real-time farmer directories and live harvest queues.
- **Why It Matters for Business**:
  - Gives operations teams, warehouse managers, and dispatch coordinators real-time oversight of current inventory across all participating farming clusters.

---

## 👥 Who Benefits from Catena?

| Stakeholder | Value Delivered |
| :--- | :--- |
| **Smallholder Farmers** | Access to transparent daily market prices, instant digital receipts, zero connectivity costs, and direct connections to verified buyers. |
| **Agricultural Aggregators & Off-Takers** | Reliable real-time crop yield forecasts, automated supplier directories, and verified procurement records. |
| **Logistics & Cold-Chain Operators** | Efficient fleet routing, optimized truck dispatch, minimized empty runs, and reduced transit spoilage. |
| **Financial Institutions & Insurers** | Verifiable digital harvest histories that enable credit assessment and risk management for rural lending. |

---

## 🚀 How to Get the App Running

Follow these step-by-step instructions to run Catena locally and connect it to telecom networks using Africa's Talking.

### Prerequisites

- **Python 3.9+** installed on your system
- An active [Africa's Talking](https://africastalking.com/) account (Sandbox is free)
- [ngrok](https://ngrok.com/) installed (for exposing your local server to telecom webhooks)

---

### Step 1: Clone the Repository & Install Dependencies

```bash
git clone https://github.com/<your-username>/catena.git
cd catena
```

Create a virtual environment (optional but recommended) and install dependencies:

```bash
# On Windows (PowerShell):
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# Install required packages:
pip install -r requirements.txt
```

---

### Step 2: Configure Environment Variables

Create your local `.env` configuration from the provided template:

```bash
cp .env.example .env
```

Open `.env` in your editor and enter your Africa's Talking credentials:

```env
AT_USERNAME=sandbox
AT_API_KEY=your_africas_talking_sandbox_api_key_here
AT_PHONE_NUMBER=+234XXXXXXXXX  # (Optional) Virtual number for voice calls
```

> **Note**: If `AT_API_KEY` is left blank, the application will run in offline simulation mode: SMS messages and Voice calls will print to the console instead of sending live telecom signals, allowing menu logic testing without an active API key.

---

### Step 3: Launch the Flask Server

Start the local server on port `5000`:

```bash
python app.py
```

You should see output confirming the server is listening:
```text
 * Running on http://0.0.0.0:5000
```

---

### Step 4: Expose Local Server via ngrok

Because telecom carriers send webhooks over the public internet, use `ngrok` in a separate terminal window to create an encrypted tunnel to your local server:

```bash
ngrok http 5000
```

Copy the forwarding HTTPS URL provided by ngrok (e.g., `https://a1b2-c3d4.ngrok-free.app`).

---

### Step 5: Configure Africa's Talking Sandbox

1. Go to the [Africa's Talking Sandbox Dashboard](https://account.africastalking.com/).
2. **Configure USSD**:
   - Go to **USSD** ➔ **Service Codes** ➔ **Create Channel**.
   - Set your channel code (e.g., `*384*1#`).
   - Set the **Callback URL** to:
     ```text
     https://<your-ngrok-url>.ngrok-free.app/ussd
     ```
3. **Configure Voice (Optional)**:
   - Go to **Voice** ➔ **Phone Numbers**.
   - Set the **Callback URL** to:
     ```text
     https://<your-ngrok-url>.ngrok-free.app/voice
     ```

---

### Step 6: Test the System

1. In the Africa's Talking Sandbox Dashboard, launch the **Web Simulator** (or open the Android Simulator app).
2. Dial your configured service code (e.g., `*384*1#`).
3. Walk through the interactive menu:
   - **Option 1**: Register as a new supplier.
   - **Option 2**: Report a harvest (observe the instant SMS receipt logged).
   - **Option 3**: Query daily commodity prices.
4. Visit `http://localhost:5000/debug/state` in your browser at any time to verify that your farmer registration and harvest records have been captured.

---

## 🐳 Docker Containerization & Deployment

Catena ships with a production-ready `Dockerfile` so you can package and deploy the entire application as a portable container — no Python environment setup required on the target server.

### Option A: Run with Docker Locally

Build and run the container on your own machine:

```bash
# Build the image
docker build -t catena .

# Run it (pass your .env file for credentials)
docker run -p 5000:5000 --env-file .env catena
```

The app will be available at `http://localhost:5000`. You can still use ngrok to expose it to Africa's Talking for sandbox testing.

---

### Option B: Push to GitHub Container Registry (Manual Push)

To deploy on a remote server or share the image, push it to [GitHub Container Registry (ghcr.io)](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry):

#### 1. Authenticate with ghcr.io

Generate a [Personal Access Token (classic)](https://github.com/settings/tokens) with `write:packages` and `read:packages` scopes, then log in:

```bash
echo YOUR_GITHUB_PAT | docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin
```

#### 2. Build, Tag & Push

```bash
# Build and tag for the registry
docker build -t ghcr.io/bnusmann22/catena:latest .

# Push to ghcr.io
docker push ghcr.io/bnusmann22/catena:latest
```

#### 3. Pull & Run Anywhere

On any server with Docker installed:

```bash
docker pull ghcr.io/bnusmann22/catena:latest
docker run -d -p 5000:5000 \
  -e AT_USERNAME=sandbox \
  -e AT_API_KEY=your_key_here \
  -e AT_PHONE_NUMBER=+234XXXXXXXXX \
  ghcr.io/bnusmann22/catena:latest
```

---

### Production Architecture

When deployed to a cloud provider, the architecture eliminates the need for ngrok:

```
                        ┌──────────────────────────────────┐
  Farmer's Phone        │         Cloud Provider           │
  (USSD / Voice)        │  (AWS, Azure, GCP, DigitalOcean) │
       │                │                                  │
       ▼                │   ┌──────────────────────────┐   │
┌─────────────┐         │   │   Docker Container       │   │
│  Africa's   │ webhook │   │  ┌────────────────────┐  │   │
│  Talking    │────────▶│   │  │  Gunicorn (4 wkrs) │  │   │
│  Gateway    │◀────────│   │  │  Flask + AT SDK    │  │   │
└─────────────┘  XML/   │   │  └────────────────────┘  │   │
               text     │   │       Port 5000          │   │
                        │   └──────────────────────────┘   │
                        └──────────────────────────────────┘
```

### Deployment Checklist

| Step | Command / Action |
| :--- | :--- |
| Build image | `docker build -t ghcr.io/bnusmann22/catena:latest .` |
| Push to registry | `docker push ghcr.io/bnusmann22/catena:latest` |
| Pull on server | `docker pull ghcr.io/bnusmann22/catena:latest` |
| Run container | `docker run -d -p 5000:5000 --env-file .env ghcr.io/bnusmann22/catena:latest` |
| Set AT USSD callback | `https://your-server-domain.com/ussd` |
| Set AT Voice callback | `https://your-server-domain.com/voice` |

> **Tip**: In production, place an HTTPS reverse proxy (e.g., Nginx, Caddy, or a cloud load balancer) in front of the container to handle TLS termination. Africa's Talking requires HTTPS callback URLs.

---

## 🔍 API & Webhook Endpoints

| Endpoint | Method | Purpose |
| :--- | :--- | :--- |
| `/` | `GET` | Health check — confirms the service is running |
| `/ussd` | `POST` | USSD webhook — receives menu interactions from Africa's Talking |
| `/voice` | `POST` | Voice webhook — handles inbound IVR calls and outbound confirmations |
| `/voice/menu` | `POST` | Voice sub-route — processes main menu DTMF selection |
| `/voice/price-result` | `POST` | Voice sub-route — reads back selected commodity price |
| `/debug/state` | `GET` | Dev-only — inspect in-memory suppliers and harvest logs |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
