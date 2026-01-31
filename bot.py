import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])

app = Flask(__name__)

application = Application.builder().token(BOT_TOKEN).build()

# --- COMMAND ---
async def start(update: Update, context):
    await update.message.reply_text("Bot aktivdir ✅")

application.add_handler(CommandHandler("start", start))

# --- WEBHOOK ---
@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "ok"

# --- TEST PAGE ---
@app.route("/", methods=["GET"])
def index():
    return "Bot is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
