python
import logging
import time
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from commands.kick import kick
from commands.unban import unban
from commands.help_cmd import help_command
from commands.info import info
from commands.ttp import ttp
from commands.lirik import lirik
from commands.ass import ass
from commands.boobs import boobs
from commands.hboobs import hboobs
from commands.ipinfo import ipinfo
from commands.darkgen import darkgen
from commands.darkweather import darkweather
from commands.defdark import defdark
from commands.darkquote import darkquote
from commands.ping import ping
from commands.uptime import uptime
from commands.nsfw import nsfw
from commands.ai_kyo import ai_kyo
from commands.ban import ban
from commands.mute import mute
from commands.unmute import unmute
from commands.nightmode import nightmode
from commands.lock import lock
from commands.tagall import tagall

TOKEN = "8449034813:AAFr7oASZ5MO_cv_W8Lffm-9c21YRIDCkYY"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level= logging.INFO)
Flask app pour une page web (optionnel)
app_flask = Flask(_name_)

@app_flask.route("/")
def home():
    return "Bot Telegram DarkAI est en ligne ✅"

Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔮 Bienvenue dans DarkAI Bot.\nTape /help pour voir les commandes.")

def start_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.bot_data["start_time"] = time.time()

    # Ajout des commandes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("kick", kick))
    app.add_handler(CommandHandler("unban", unban))
    app.add_handler(CommandHandler("ban", ban))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("ipinfo", ipinfo))
    app.add_handler(CommandHandler("ttp", ttp))
    app.add_handler(CommandHandler("lirik", lirik))
    app.add_handler(CommandHandler("ass", ass))
    app.add_handler(CommandHandler("boobs", boobs))
    app.add_handler(CommandHandler("hboobs", hboobs))
    app.add_handler(CommandHandler("darkgen", darkgen))
    app.add_handler(CommandHandler("darkweather", darkweather))
    app.add_handler(CommandHandler("defdark", defdark))
    app.add_handler(CommandHandler("darkquote", darkquote))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("uptime", uptime))
    app.add_handler(CommandHandler("nsfw", nsfw))
    app.add_handler(CommandHandler("mute", mute))
    app.add_handler(CommandHandler("unmute", unmute))
    app.add_handler(CommandHandler("nightmode", nightmode))
    app.add_handler(CommandHandler("lock", lock))
    app.add_handler(CommandHandler("tagall", tagall))
    app.add_handler(CommandHandler(["ai", "kyo"], ai_kyo))

    app.run_polling()

if _name_ == "_main_":
    # Démarrer le bot dans un thread
    threading.Thread(target=start_bot).start()
    # Démarrer le serveur Flask (optionnel)
    app_flask.run(host="0.0.0.0", port=10000)
