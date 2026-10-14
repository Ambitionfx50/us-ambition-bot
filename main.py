import os, threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
TOKEN=os.getenv("BOT_TOKEN")
async def start(update,context): await update.message.reply_text("🚀 Welcome to US AMBITION AI GLOBAL!\n@USAmbitionAIBot - Official Assistant\n\n✅ /start /help /about /contact /services")
async def help_cmd(update,context): await update.message.reply_text("💡 Send any message! Contact: ambitionfx50@gmail.com")
async def about(update,context): await update.message.reply_text("🏢 US AMBITION AI GLOBAL\nAI bots & automation. Founder: Ambitionfx50")
async def contact(update,context): await update.message.reply_text("📞 @USAmbitionAIBot\nEmail: ambitionfx50@gmail.com")
async def services(update,context): await update.message.reply_text("🔥 Services:\n1. Telegram Bots\n2. Crypto Automation\n3. AI Agents")
async def echo(update,context): await update.message.reply_text(f"You said: {update.message.text}")
def run_bot():
    app=Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start",start)); app.add_handler(CommandHandler("help",help_cmd)); app.add_handler(CommandHandler("about",about)); app.add_handler(CommandHandler("contact",contact)); app.add_handler(CommandHandler("services",services))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,echo))
    app.run_polling()
flask_app=Flask(__name__)
@flask_app.route('/')
def home(): return "US AMBITION AI GLOBAL Bot is Live!"
if __name__=="__main__":
    threading.Thread(target=run_bot,daemon=True).start()
    flask_app.run(host="0.0.0.0",port=int(os.environ.get("PORT",10000)))
