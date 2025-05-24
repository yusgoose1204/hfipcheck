from slack_bolt import App
from dotenv import load_dotenv
import os
from hfipcheck import check_ip

load_dotenv()

slack_bolt_app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
)

@slack_bolt_app.command("/hfipcheck")
def handle_command(ack, respond, command):
    print("✅ Slash command triggered:", command)
    ack()
    ip = command["text"].strip()
    result = check_ip(ip)
    respond(result)


