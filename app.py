import os
import logging

import dotenv
import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

dotenv.load_dotenv()

logging.basicConfig(level=logging.INFO)


app = App(token=os.environ["SLACK_BOT_TOKEN"])


@app.message("^.*【通報】コミュニティに通報がありました。.*$")
def hello(say):
    say("<@UUHFHSYEL>")


@app.event("app_mention")
def say_when_app_mention(say):
    say("Shut up.")


@app.message("^.*<>.*$".format("UC734HMC4"))
def say_when_some_mention(say):
    say("He is busy.")


@app.message("hungry")
def say_with_mention(say):
    say("<@{}>\nGo to Fukushimaya.".format("UC734HMC4"))


@app.message("help")
def say_on_other_channel(message, say):
    say(
        "<@{}> is asking for help in <#{}>.".format(
            message["user"], message["channel"]
        ),
        channel="C02JD5ATBH7",
    )


@app.message("draw")
def draw(say):
    r = requests.get("https://db.ygoprodeck.com/api/v7/randomcard.php")
    j = r.json()

    say(j["card_images"][0]["image_url"])


@app.message("test")
def say_message_body(message, say):
    say(str(message))


if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
