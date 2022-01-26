import re
import requests
from urllib import request

# for HTTP purpose
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Link:
    # find a value in a string, meant for long string 
    def findKey(regex: re.Pattern, html: str, key_ind: int = 0) -> str:
        key = regex.findall(html)
        if key is None or key == '' or key == []:
            print("¯\_(ツ)_/¯")
        else:            
            key = str(key[key_ind])
            return key
        return False

    # downloading HTTP pages
    def reach_schedule(link: str) -> str:
        with request.urlopen(link) as response:
            html = response.read()    
        return html.decode("utf-8")
    
    # downloading HTTPS pages
    def reach_HTTPSchedule(link: str) -> str:
        r = requests.get(link)
        return str(r.text)

# ==============================================================================================================================================                                      
# |                                                                                         | Double Trouble                                   |
# |                                           #                                             |     project: cobiachi_bot                        |
# |                                          ###                                            |     date: 2021-10-12                             |
# |                                         #####                                           |     file description:                            |
# |                     ############        #####        ###########                        |     module for downloading html files and        |
# |               ######################   #######   #########################              |     scavenging it.                               |
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
                                                                               
                                                                                                                               