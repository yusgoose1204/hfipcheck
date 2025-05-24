# HFIPcheck – Production Deployment Notes

This document outlines the key steps and best practices to follow when transitioning the HFIPcheck Slack bot from development to production.

---

## ✅ HFIPcheck: Production-Readiness Checklist

### 📦 1. Move Off Cloudflare Quick Tunnel
- **Why**: Quick tunnels are temporary and not suitable for production.
- **Use Instead**:
  - [Render](https://render.com) – easiest for deploying Flask apps
  - Fly.io, Railway, or AWS Lambda + API Gateway
- **Ensure**: A public, always-on HTTPS endpoint like:
  ```
  https://yourcompany.com/slack/events
  ```

---

### 🔐 2. Proper Secret Management
- **Current**: `.env` file with `SLACK_BOT_TOKEN` and `SLACK_SIGNING_SECRET`
- **Production**:
  - Never commit `.env` to Git
  - Use environment variables or a secrets manager
  - Services like Render provide secure secret injection

---

### 🛡 3. Security Hardening
- Slack Bolt already verifies requests using the signing secret
- Sanitize user input before echoing it back
- Add user/channel restrictions if needed

---

### 📈 4. Logging & Monitoring
- Add logs for:
  - User input
  - IP check result
  - Errors
- Tools to consider:
  - `loguru`, `structlog`
  - External: Papertrail, Logtail, AWS CloudWatch

---

### 🧪 5. Testing
- Add unit tests for:
  - `check_ip()`
  - Slash command handler (mocked)
- Use `pytest` and Flask's test client

---

### 📄 6. Documentation
- Include:
  - `README.md`
  - `.env.example`
  - Setup instructions
  - Sample payloads or usage

---

### 🚦 7. Slack Workspace Installation
- Work with Slack Admin to:
  - Approve app scopes: `commands`, `chat:write`
  - Approve slash command endpoint
- Ensure app is invited to relevant channels:
  ```
  /invite @HFIPcheck
  ```

---

### ✅ 8. Optional Feature Improvements
- Support multiple IPs: `/hfipcheck ip1, ip2`
- Show region names in output
- Allow `/hfipcheck --public` for visible messages

---

## 🧠 Lessons from Troubleshooting

| Issue | Root Cause | Fix |
|-------|------------|-----|
| `dispatch_failed` | Flask wasn't reachable | Setup Cloudflare tunnel correctly |
| No terminal logs | Tunnel expired | Restart Flask + Cloudflare with new URL |
| `dispatch_unknown_error` | Slack handler not triggered | Fixed bot install and correct function registration |
| `App has no handler` | Missing Flask adapter | Used `SlackRequestHandler` |
| Command unresponsive | URL mismatch | Updated Slack slash command config |

---

**Ready for Launch?** ✅ Push to a production host, secure your secrets, and you're good to go!