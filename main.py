"""
So basically the main reason for this is to use a website known as bypass.vip to bypass linkvertise links easily without having to open 20 different tabs
it was supposed to be easy and it was until i realized that the api was broken
remember to also register the commands in @BotFather
"""
from telegram.ext import Updater, MessageHandler, filters, Application, CommandHandler, ContextTypes
from telegram import Update
import requests
import validators

TOKEN = 'TOKEN HERE'


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Send me a link and i will use bypass.vip to bypass it and return it to you!')


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Send me a link and i will use bypass.vip to bypass it and return it to you!')


async def links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_text = update.message.text
    print(msg_text)
    if validators.url(msg_text):
        payload = {
            "url": msg_text,
        }
        r = requests.post("https://api.bypass.vip/", data=payload) # the api i tried to use
        final_link = r.json()
        print(f"{r.json()}")
        await update.message.reply_text(f"Here is your bypassed link! {final_link["destination"]}")
        await update.message.reply_text(f"dev mode:\n{final_link}")

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

if __name__ == '__main__':
    print("Starting bot")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('start', start_command))
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, links))
    # Errors
    app.add_error_handler(error)
    # Poll the bot
    print("Polling..")
    app.run_polling(poll_interval=3)
