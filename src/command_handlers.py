"""
This file contains the command handlers for the bot.
"""
import logging
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

def start(update: Update, context: CallbackContext):
    """
    Send a message when the command /start is issued.
    
    args:
        update: Update object
        context: CallbackContext object
    """
    logging.info('Command /start received from ' + update.effective_user.full_name + '.')
    update.message.reply_text('Hi!')

if __name__ == '__main__':
    print('This file is not meant to be run directly.')