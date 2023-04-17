import os
import flask
import telebot
from datetime import datetime
from pytz import timezone

TELEGRAM_BOT_KEY = os.environ.get("telegram_bot_key")
app = flask.Flask(__name__)
bot = telebot.TeleBot(TG_BOT_KEY)


# non-command message
@bot.message_handler(commands=["start"])
@bot.message_handler(func=lambda m: True)
def chat(message):
    msg = "我只是个报时器"
    bot.send_message(message.chat.id, msg)


# We use telegram_bot_key as the web hook route
@app.route(f"/{TELEGRAM_BOT_KEY}", methods=["POST"])
def getMessage():
    bot.process_new_updates(
        [telebot.types.Update.de_json(flask.request.stream.read().decode("utf-8"))]
    )
    return "!"


@app.route("/")
def index():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://reverse-tg-bot.azurewebsites.net/{TELEGRAM_BOT_KEY}")

    LA = timezone("America/Los_Angeles")
    Copenhagen = timezone("Europe/Copenhagen")
    SH = timezone("Asia/Shanghai")
    Tokyo = timezone("Asia/Tokyo")
    fmt = "%H:%M"

    msg = f"""🇺🇸 {datetime.now(LA).strftime(fmt)}
🇩🇰 {datetime.now(Copenhagen).strftime(fmt)}
🇭🇰 {datetime.now(SH).strftime(fmt)}
🇯🇵 {datetime.now(Tokyo).strftime(fmt)}"""
    bot.send_message(-1937998371, msg)
    return "我只是个报时器"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
