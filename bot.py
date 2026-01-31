import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))

bot = Bot(token=BOT_TOKEN)

app = Flask(__name__)

# --- TELEGRAM COMMAND ---
async def start(update: Update, context):
    await update.message.reply_text("Bot aktivdir ✅")

# --- APPLICATION ---
application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))

# --- WEBHOOK ROUTE ---
@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    application.update_queue.put_nowait(update)
    return "ok"

# --- HEALTH CHECK ---
@app.route("/", methods=["GET"])
def index():
    return "Bot is running"

# --- START ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
