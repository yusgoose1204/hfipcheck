from flask import Flask, request
from slack_handler import slack_bolt_app  # Must match variable name in slack_handler.py

flask_app = Flask(__name__)

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    print("🚨 Slack event received")
    return slack_bolt_app.dispatch(request)
