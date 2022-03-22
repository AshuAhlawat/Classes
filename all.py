RECORD = {
    #your_name : [registration number , password]
}


import sys
from script import onlineclassscript

import os
import threading


args_arr = sys.argv

PEOPLE = []

for i in args_arr:
    PEOPLE.append(i)
    
methods = ["Microphone","Listen only"]
METHOD = methods[0]
NO_SCREEN = False
MUTE = True
SOUND = False

system = os.uname()[0]

if system == "Linux":
    ROOT = "./chromedriver98"
else:
    ROOT = "./chromedriver97.exe"

if "help" in PEOPLE:
    print("---------Welcome to ClassScript---------")
    print("Follow the steps to attend class:")
    help_man = '''(1)Open you class script folder in terminal.
                  (2)now run python3 or python all.py args
                  (3) arguments are :
                   -ankit,ashu,sarthak,gaurav,shrayansh,rishika and  help for This page'''
    print(help_man)
    quit()


def run(name, reg_no, password):
    onlineclassscript(name, reg_no, password,ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN,sound=SOUND)

print("Selected people are:")

try:
    for i in range(1,len(PEOPLE)):
        print(PEOPLE[i])

        thread = threading.Thread(target=run, args=[PEOPLE[i], RECORD[PEOPLE[i]][0], RECORD[PEOPLE[i]][1]])

        thread.start()
except:
    print("Wrong Input Try Again")
    sys.exit()