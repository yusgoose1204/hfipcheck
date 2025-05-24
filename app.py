from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_handler import slack_bolt_app

flask_app = Flask(__name__)
handler = SlackRequestHandler(slack_bolt_app)

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    print("🚨 Slack event received")
    return handler.handle(request)