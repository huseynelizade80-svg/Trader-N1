from telegram import Bot
from flask import Flask, request
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))

bot = Bot(token=BOT_TOKEN)

@app.route("/signal", methods=["POST"])
def signal():
    data = request.json

    pair = data.get("pair", "BTC/USDT")
    side = data.get("side", "LONG")
    tp = data.get("tp", "—")
    sl = data.get("sl", "—")

    text = (
        "📊 SİQNAL\n"
        f"Cütlük: {pair}\n"
        f"İstiqamət: {side}\n"
        f"TP: {tp}\n"
        f"SL: {sl}"
    )

    bot.send_message(chat_id=CHANNEL_ID, text=text)
    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
