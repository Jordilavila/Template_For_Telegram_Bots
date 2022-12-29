"""
This is the main file of the bot. It contains the main function and the main loop.
"""
import os, logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

from src.command_handlers import start
from src.message_handlers import save_the_chat_when_bot_joins

load_dotenv()
updater = Updater(token=os.getenv('TELEGRAM_BOT_TOKEN'), use_context=True)
dp = updater.dispatcher
jq = updater.job_queue

### Command Handlers ###
dp.add_handler(CommandHandler('start', start))

### Message Handlers ###
dp.add_handler(MessageHandler(Filters.text, save_the_chat_when_bot_joins))

### Job Queue ###

### Conversation Handlers ###

### Main Loop ###

if __name__ == '__main__':
    ## Clean past logs:
    open(os.getenv('Log_Folder') + os.getenv('Log_File'), 'w').close()

    ## Set up logging:
    logging.basicConfig(datefmt=os.getenv('DT_Format'),
                        format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO,
                        filename=os.getenv('Log_Folder') + os.getenv('Log_File'))

    ## Start the bot:
    updater.start_polling()
    logging.info('Bot started.')
    print('Bot started.')
    updater.idle()