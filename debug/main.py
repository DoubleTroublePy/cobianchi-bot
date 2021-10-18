from telegram_class import telegram
from link_class import link as lc

from threading import Thread
import datetime
import time
import json
import os
import re

class linkFind(Thread):
    def __init__(self, nome, path):
        Thread.__init__(self)
        self.nome = nome
        self.path = path

    def run(self):
        # analize a path
        def path_analisis(path:str, string:str, rew:bool = False):
            if os.path.exists(path):
                with open(path, 'r+') as f: #if exist read else create the file
                    link = f.readlines()
                return link
            elif rew:
                with open(path, 'w') as f:
                    link = string
                return False
        # assemble a link and reach them
        key = 'http://www.cobianchi.it/'
        data = datetime.datetime.now()
        year = data.year
        key1 = 'orario/orario'

        if data.month < 9:
            key1 = str(key1 + str(year-1) + "-" + str(int(str(year)[2:4])))
        else:
            key1 = str(key1 + str(year) + "-" + str(int(str(year)[2:4])+1))
            key2 = '/versione-'
            key3 = '"'
            
            html_file = lc.reachSchedule(key)
            html_link = lc.findKey(re.compile(key1 + key2 + '(.*?)' + key3), html_file)
            link = path_analisis(self.path, '')
            if html_link != link:
                with open(self.path, 'w') as f:
                    f.write(key + key1 + key2 + html_link)      
                return html_link

if __name__ == '__main__':

    path = '/Users/DoubleTroublePy/Documents/Programmi/GitHub/Progetti/cobianchi-bot/link.txt'

    time_start = time.time()
    message_val = 0
    
    timer_0 = time.time()
    timer_1 = time.time() + 86500
    timer_2 = time.time() + 3
    
    thread1 = linkFind("link", path)

    while True:
        try:
                
            if abs(timer_1 - time.time()) >= 86400:
                thread1.start()
                with open(path, 'r') as f:
                    link = f.read()
                timer_1 = time.time()

            # get a telegram update
            if abs(timer_2 - time.time()) >= 1:
                update = telegram.bot_get_update()
                update = update.read()
                update = json.loads(update)
                timer_2 = time.time()

                # navigate in the json file
                if 'update' in globals() and update['ok'] and update["result"] != []:
                    if "message" in update["result"][0]:
                        for pos in range(len(update["result"])):

                            message = update["result"][pos]["message"]["text"]
                            ID = str(update["result"][pos]["message"]["chat"]["id"])
                            first_name = str(update["result"][pos]["message"]["from"]["first_name"])
                
                            message_val += 1

                            if '/start' in message:
                                text = 'comandi a disposizione: \n /orario <classe> se usato puro restituscie l orario generale'
                                telegram.bot_send_text(text, ID)

                            if '/orario'in message: # command /orario <classe>
                                if len(message) == 7: # if the class in not present send the general link
                                    telegram.bot_send_text('Nuovo orario >>> ' + link, ID)
                                elif len(message) == 13: 
                                    class_val = message[8:] # delete /orario part
                                    class_val = class_val.upper() 
                                    html_file = lc.reachSchedule(link)
                                    patt = re.compile('<A HREF="(.*?).html" class = \'mathema\'>' + class_val)
                                    link_val2 = lc.findKey(patt, html_file)
                                    if link_val2: # if the program find the class send it, else send an error
                                        telegram.bot_send_text("l'orario della " + class_val + " è >>> " + link + '/' + link_val2 + '.html', ID)
                                    else:
                                        telegram.bot_send_text("classe incorretta o inesistente", ID)
                                else:
                                    telegram.bot_send_text("classe incorretta", ID)
                    # set the offset to the next value
                    telegram.bot_set_offset(str((update["result"][len(update["result"])-1]["update_id"]) + 1))

            print('\n' * 100)
            print('eta :: ', str(round(abs(time_start - time.time()), 0)))
            print(str(message_val), 'message')
        except:
            print('\n' * 100)
            print('eta :: ', str(round(abs(time_start - time.time()), 0)))
            print('error')
        time.sleep(0.05)
        

# ==============================================================================================================================================                                      
# |                                                                                         | Double Trouble                                   |
# |                                           #                                             |     project: cobiachi_bot                        |
# |                                          ###                                            |     date: 2021-10-12                             |
# |                                         #####                                           |     file description:                            |
# |                     ############        #####        ###########                        |                                                  |
# |               ######################   #######   #########################              |                                                  |
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
                                                                               
                                                                                                                               