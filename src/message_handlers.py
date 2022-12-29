"""
This file contains the message handlers for the bot.
"""
import logging
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

from src.utils import get_bd, post_bd, getFormatedDT

def save_the_chat_when_bot_joins(update: Update, context: CallbackContext):
    """
    Save the chat when the bot joins a group.
    
    args:
        update: Update object
        context: CallbackContext object
    """
    logging.info('Bot joined group ' + update.effective_chat.title + '.')
    for member in update.message.new_chat_members:
        if member.id == context.bot.id:
            save_group_in_database(update, context)
            break

def save_group_in_database(update: Update, context: CallbackContext):
    """
    Save the group in the database.
    
    args:
        update: Update object
        context: CallbackContext object
    """
    logging.info('Saving group ' + update.effective_chat.title + ' in database.')

    if update.effective_chat.title in chats_list_by_name():
        logging.info('Group ' + update.effective_chat.title + ' already in database.')
        return
    
    new_group = {
        'id': update.effective_chat.id,
        'title': update.effective_chat.title,
        'link': update.effective_chat.link,
        'type': update.effective_chat.type,
        'joined_on': getFormatedDT()
    }

    if chats_post_new(new_group):
        logging.info('Group ' + update.effective_chat.title + ' saved in database.')
        update.effective_chat.send_message('Hello, I\'m the new bot of this group. I\'ll be here to help you with your tasks.')
    else:
        logging.error('Error saving group ' + update.effective_chat.title + ' in database.')
        update.effective_chat.send_message('Hello, I\'m the new bot of this group. I\'m having some trouble saving the group in the database. Please, contact the administrator. \nSee you later.')
        update.effective_chat.leave()

def chats_list_by_name() -> list:
    """
    Return a list of the names of all the chats in the database.
    
    returns:
        list of str
    """
    groups = get_bd('chats.json')
    return [group['name'] for group in groups]

def chats_post_new(group:dict) -> bool:
    """
    Post a new group in the database.
    
    args:
        group: dict
    
    returns:
        bool
    """
    chatsbd:dict = get_bd('chats.json')
    if not groups_check(group['id']):
        chatsbd['chats'].append(group)
        return post_bd('chats.json', chatsbd)

def groups_check(group_id:int) -> bool:
    """
    Check if a group is already in the database.
    
    args:
        group_id: int
    
    returns:
        True if the group is in the database, False otherwise
    """
    chats:list = get_bd('chats.json')['chats']
    for chat in chats:
        if chat['id'] == group_id:
            return True
    return False

if __name__ == '__main__':
    print('This file is not meant to be run directly.')