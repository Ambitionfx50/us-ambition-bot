import os
import threading
from flask import Flask
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# --- Telegram Bot Commands ---
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🇺🇸 Welcome to US AMBITION AI GLOBAL! 🚀\n\nYour AI assistant is LIVE and working!\n\nSend /help to see what I can do.")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "I can help you with:\n✅ US Visa & Jobs Info\n✅ AI Tools\n✅ Business Ideas\n\nJust type your question!")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"You said: {message.text}\n\nI'm US Ambition AI - How can I help you today?")

# --- Flask for Render ---
app = Flask(__name__)

@app.route('/')
def home():
    return "US AMBITION BOT IS LIVE! @USAmbitionAIBot is running."

def run_bot():
    print("Starting Telegram bot polling...")
    bot.infinity_polling()

if __name__ == "__main__":
    # Start bot in background thread
    threading.Thread(target=run_bot, daemon=True).start()
    # Start Flask
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)8759701719:AAFU9h4g7Vps6pF9alCD9GnHsAfC_5084Jw