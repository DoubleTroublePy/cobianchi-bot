from os import getenv
from requests import get
from urllib.request import urlopen
from dotenv import load_dotenv
import json
import requests

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Telegram:
    def bot_set_offset(offset:str) -> json:
        # retrieve the telegram token
        load_dotenv()
        TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')
        # compose link api
        send_text = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates?offset={offset}'
        
        # post the html link
        response = urlopen(send_text)
        return response

    def bot_get_update(self) -> urlopen:
        # retrive the telegram token
        load_dotenv()
        TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')

        send_text = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates'

        # post the html link
        response = urlopen(send_text)
        return response

    def bot_send_text(bot_message: str, chat_id: str) -> json:
        # retrieve the telegram token
        load_dotenv()
        TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')

        send_text = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/' \
                    f'sendMessage?chat_id={chat_id}&' \
                    f'parse_mode=Markdown&' \
                    f'text={bot_message}'

        # make a get request api
        response = get(send_text)
        return response.json()

# ==============================================================================================================================================                                      
# |                                                                                         | Double Trouble                                   |
# |                                           #                                             |     project: cobiachi_bot                        |
# |                                          ###                                            |     date: 2021-10-12                             |
# |                                         #####                                           |     file description:                            |
# |                     ############        #####        ###########                        |     personalized module for telegram i dont like |
# |               ######################   #######   #########################              |     the standard one.                            |
# |           ####################################################################          |                                                  |
# |       ############################################################################      |                                                  |
# |    #################################################################################    |                                                  |
# |            ######   #################  #######  #################   #######             |                                                  |
# |                                         #####                                           |--------------------------------------------------|
# |                                         #####                                           | Social                                           |
# |                                        #######                                          |     Github: http://github.com/DoubleTroublePy    |
# |                                       #########                                         |     Twitter: @DoubleTroublePy                    |
# |                                                                                         |                                                  |
# ==============================================================================================================================================
                                                                               
                                                                                                                               