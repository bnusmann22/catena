# Catena — USSD Agricultural Data Capture & Logistics

**Catena** is a lightweight, accessible USSD application built with Python and Flask. Designed for agricultural supply chains and smallholder farmers, Catena enables seamless produce reporting, farmer registration, and real-time market price lookups over standard USSD channels with automated SMS receipts powered by **Africa's Talking**.

---

## 🌾 Features

- **Farmer & Supplier Registration**: Quick onboarding menu allowing farmers to register their phone number, name, and primary crop/produce.
- **Harvest Logging & Reporting**: Allows farmers to submit real-time harvest records (crop type and quantity in kilograms).
- **Automated SMS Receipts**: Fires immediate confirmation SMS messages to farmers upon logging a harvest report using Africa's Talking SMS API.
- **Commodity Price Queries**: Instant USSD lookup for daily agricultural commodity prices (e.g., Cassava, Maize, Yam, Rice) in local currency (₦/kg).
- **Debug & Inspection API**: A simple `/debug/state` REST endpoint for developers to view active in-memory suppliers and harvest logs.

---

## 📲 USSD Menu Navigation Tree

```text
Root Menu (*384*1#)
 ├── 1. Register as supplier
 │    ├── Enter your name
 │    └── Enter produce type (e.g., Cassava) ──> [Registered & Saved]
 ├── 2. Report harvest
 │    ├── Enter produce type
 │    └── Enter quantity in kg ──> [Logged & SMS Notification Sent]
 └── 3. Check today's price
      ├── 1. Cassava
      ├── 2. Maize
      ├── 3. Yam
      └── 4. Rice ──> [Returns Today's Price per kg]
```

---

## 🛠️ Technology Stack

- **Backend Framework**: Python 3.x, [Flask](https://flask.palletsprojects.com/)
- **Telecom Gateway**: [Africa's Talking SDK](https://africastalking.com/) (USSD & SMS API)
- **Environment Management**: `python-dotenv`
- **Tunneling / Webhook Proxy**: [ngrok](https://ngrok.com/)

---

## 🚀 Quickstart Guide

### 1. Clone & Install Dependencies

Ensure Python 3.9+ is installed. Clone the repository and install required packages:

```bash
git clone https://github.com/<your-username>/catena.git
cd catena
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Edit `.env` to include your Africa's Talking API credentials (defaults to sandbox testing):

```env
AT_USERNAME=sandbox
AT_API_KEY=your_africas_talking_api_key_here
```

> **Note**: If `AT_API_KEY` is left blank, SMS notifications will fall back to logging in the console without breaking the USSD flow.

---

## 🌐 Running Locally & Testing with Africa's Talking

### Step 1: Start the Flask Server

Run the development server on port `5000`:

```bash
python app.py
```

### Step 2: Expose Webhook via ngrok

In a separate terminal, launch `ngrok` to expose your local Flask app to the internet:

```bash
ngrok http 5000
```

Copy the generated HTTPS URL (e.g., `https://abc1234.ngrok-free.app`).

### Step 3: Configure Africa's Talking Sandbox

1. Log into the [Africa's Talking Sandbox Dashboard](https://account.africastalking.com/).
2. Navigate to **USSD** > **Create Channel**.
3. Set your **Service Code** (e.g., `*384*1#`).
4. Set the **Callback URL** to:
   ```text
   https://<your-ngrok-url>.ngrok-free.app/ussd
   ```
5. Launch the **Africa's Talking Web Simulator** to test menu navigation.

---

## 🔍 API & Inspection Endpoints

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/ussd` | `POST` | Primary webhook for Africa's Talking USSD HTTP requests |
| `/debug/state` | `GET` | View current in-memory suppliers and harvest log data |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
