from os import getenv
from requests import get
from urllib.request import urlopen
from dotenv import load_dotenv
import json
import requests

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class telegram:
    def bot_set_offset(offset:str) -> json:
        # retrive the telegram token
        load_dotenv()
        TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')
        #compose link api
        send_text =  'https://api.telegram.org/bot' + TELEGRAM_TOKEN + '/getUpdates?offset=' + offset
        
        # post the html link
        response = urlopen(send_text)
        return response

    def bot_get_update() -> urlopen:
        # retrive the telegram token
        load_dotenv()
        TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')

        send_text =  'https://api.telegram.org/bot' + TELEGRAM_TOKEN + '/getUpdates'

        # post the html link
        response = urlopen(send_text)
        return response

    def bot_send_text(bot_message:str, chat_id:str) -> json:
        # retrive the telegram token
        load_dotenv()
        TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')

        send_text = 'https://api.telegram.org/bot' + TELEGRAM_TOKEN + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message

        #make a get request api
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
                                                                               
                                                                                                                               