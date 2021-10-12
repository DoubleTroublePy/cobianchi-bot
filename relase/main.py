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
        print ("... " + self.name + " start ...")
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
                    print('... writing ...')
                    f.write(key + key1 + key2 + html_link)      
                return html_link

if __name__ == '__main__':

    path = 'E:/GitHub/timetable-link-notification/link.txt'
    time_now = time.time() + 86500
    thread1 = linkFind("link", path)

    while True:
        time_old = time.time()
        if time_now - time_old >= 86400:
            thread1.start()
            with open(path, 'r') as f:
                link = f.read()
            time_now = time.time()
        
        # get a telegram update
        update = telegram.bot_get_update()
        update = update.read()
        update = json.loads(update)

        # navigate in the json file
        if update['ok'] and update["result"] != []:
            if "message" in update["result"][0]:
                for pos in range(len(update["result"])):

                    message = update["result"][pos]["message"]["text"]
                    ID = str(update["result"][pos]["message"]["chat"]["id"])
                    first_name = str(update["result"][pos]["message"]["from"]["first_name"])
        
                    print("... message ...")

                    if '/orario'in message: # command /orario <classe>
                        if len(message) == 7: # if the class in not present send the general link
                            telegram.bot_send_text('Nuovo orario >>> ' + link, ID)
                        elif len(message) > 7: 
                            class_val = message[8:] # delete /orario part
                            class_val = class_val.upper() 
                            html_file = lc.reachSchedule(link)
                            patt = re.compile('<A HREF="(.*?).html" class = \'mathema\'>' + class_val)
                            link_val2 = lc.findKey(patt, html_file)
                            if link_val2: # if the program find the class send it else send error
                                telegram.bot_send_text("l'orario della " + class_val + " è >>> " + link + '/' + link_val2 + '.html', ID)
                            else:
                                telegram.bot_send_text("classe incoretta o inesistente", ID)
            # set the offset to the next value
            telegram.bot_set_offset(str((update["result"][len(update["result"])-1]["update_id"]) + 1))
        time.sleep(.1)

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
                                                                               
                                                                                                                               