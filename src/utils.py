"""
This file contains utility functions for the bot.
"""
import logging, json, os

def build_menu(buttons: list, n_cols: int, header_buttons: list=None, footer_buttons: list=None) -> list:
    """
    Build a menu with buttons.
    
    args:
        buttons: list of list of InlineKeyboardButton
        n_cols: int
        header_buttons: list of InlineKeyboardButton
        footer_buttons: list of InlineKeyboardButton

    returns:
        list of list of InlineKeyboardButton
    """
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

def get_bd(file_name:str, encoding:str='utf-8') -> dict:
    """
    Get the content of a json file.
    
    args:
        file_name: str
        encoding: str

    returns:
        dict
    """
    logging.info('Getting content of ' + file_name + '.')
    with open(os.getenv("DB_Folder") + file_name, 'r') as file:
        return json.load(file)

def post_bd(file_name:str, data:dict, encoding:str='utf-8') -> bool:
    """
    Post data to a json file.
    
    args:
        file_name: str
        data: dict
        encoding: str
    """
    try:
        logging.info('Posting data to ' + file_name + '.')
        with open(os.getenv("DB_Folder") + file_name, 'w', encoding=encoding) as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True
    except:
        logging.error('Error while posting data to ' + file_name + '.')
        return False

def getFormatedDT() -> str:
    """
    Return the current date and time in the format specified in the .env file.
    
    returns:
        str
    """
    from datetime import datetime
    return datetime.now().strftime(os.getenv('DT_Format'))

if __name__ == '__main__':
    print('This file is not meant to be run directly.')