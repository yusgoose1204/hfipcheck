# ⚡ HFIPcheck – Hyperforce IP Check Slack Bot

**HFIPcheck** is a lightweight Slack bot built to help support engineers quickly verify whether an IP address belongs to Salesforce’s Hyperforce infrastructure.

Developed with Flask and Slack’s Bolt SDK, this tool enables fast IP checks directly in Slack using the `/hypercheck` command — reducing manual triage effort and empowering teammates with limited networking experience.

---

## 🚀 Features

- ✅ Validates IPs against Salesforce's official [IP ranges](https://ip-ranges.salesforce.com/ip-ranges.json)
- 🔍 Supports CIDR range matching (e.g., 141.163.208.2 matches 141.163.208.0/23)
- 🌐 Integrates directly into Slack via a custom slash command
- 🧪 Includes test harness and IP sample files
- 🔒 Secrets managed securely via `.env` (never hardcoded)

---

## 📦 Project Structure

```
hfipcheck/
├── app.py               # Flask entry point
├── slack_handler.py     # Slack command logic
├── hypercheck.py        # Core IP validation logic
├── fetch_ip_data.py     # Fetches IP ranges from Salesforce
├── ip_data.json         # Cached Salesforce IP list
├── requirements.txt     # Dependencies
├── .env                 # Slack secrets (excluded from Git)
└── test_ips/            # Sample IP files + test runner
```

---

## 🧪 Run Locally

### 1. Install Python and create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Fetch the latest IP ranges

```bash
python fetch_ip_data.py
```

### 3. Create a `.env` file with your Slack credentials

```
SLACK_BOT_TOKEN=xoxb-your-slack-token
SLACK_SIGNING_SECRET=your-signing-secret
```

### 4. Run the Flask server

```bash
flask --app app:flask_app run
```

### 5. Expose your app publicly using Cloudflare Tunnel

```bash
cloudflared tunnel --url http://localhost:5000
```

> Use the provided `https://your-url.trycloudflare.com/slack/events` as the Slack slash command request URL.

---

## 🔎 Test Without Slack

To test IP logic independently of Slack:
```bash
python test_ips/run_tests.py
```

> This will run multiple IPs (valid, invalid, edge cases) through your detection logic.

---

## 🤖 Slack Usage Example

Once connected, users in Slack can simply type:

```
/hypercheck 141.163.208.1
```

Bot response:

```
✅ IP belongs to Salesforce Hyperforce
• Region: ap-northeast-1
• Provider: aws
• CIDR: 141.163.208.0/23
```

---

## 🛡️ Security

- Slack secrets are stored in a `.env` file, never committed to Git
- Uses environment variable loading via `python-dotenv`
- Can be easily extended to cloud hosting (Render, Railway, Heroku)

---

## 🛠️ Built With

- Python 3.9+
- Flask
- Slack Bolt SDK
- Cloudflare Tunnel
- ipaddress module

---

## 🧑‍💻 Author

**Yusei Yamaguchi**  
Senior Support Engineer – Network Infrastructure  
Aspiring Software Engineer | Focused on tools that bridge ops & automation

---

## 📸 Screenshot

![HFIPcheck demo](hfipcheck-demo.png)

---

## 🧭 Flow Summary

```mermaid
sequenceDiagram
  participant U as Slack User
  participant S as Slack Server
  participant C as Cloudflare Tunnel
  participant F as Flask App

  U->>S: /hfipcheck 141.163.208.1
  S->>C: POST https://your-tunnel.trycloudflare.com/slack/events
  C->>F: POST /slack/events
  F->>F: Parse + process command
  F->>S: Respond with message
  S->>U: Display result in Slack
```


## 📝 License

This project is licensed under the [MIT License](./LICENSE).
