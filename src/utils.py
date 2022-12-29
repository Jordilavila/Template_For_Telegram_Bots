"""
This file contains utility functions for the bot.
"""
import logging, json, os

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

if __name__ == '__main__':
    print('This file is not meant to be run directly.')