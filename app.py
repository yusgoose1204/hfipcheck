from flask import Flask, request
from slack_handler import app as slack_app

flask_app = Flask(__name__)

# When a POST request hits /slack/events, pass it to the Slack handler
@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return slack_app.handler.handle(request)
