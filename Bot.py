from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '7548549501: AAGpjoqNDdqa3FxzXybUA
kmpaGXqB8ms ANO'  # Токен, который ты получишь от BotFather
CHANNEL_ID = '@kipokppppppp'  # Укажи свой канал

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я бот!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
