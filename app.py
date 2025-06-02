from flask import Flask, request
from slack_handler import slack_bolt_app
from slack_bolt.adapter.flask import SlackRequestHandler

# Create the Flask app
flask_app = Flask(__name__)

# Create a Slack request handler using your Bolt app
handler = SlackRequestHandler(slack_bolt_app)

# Route to receive Slack events
@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    print("🚨 Slack event received")
    return handler.handle(request)
