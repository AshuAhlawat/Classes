import sys
from script import onlineclassscript

import os
import threading


args_arr = sys.argv

PEOPLE = ["ashu"]

for i in args_arr:
    PEOPLE.append(i)
    
methods = ["Microphone","Listen only"]
METHOD = methods[0]
NO_SCREEN = False
MUTE = True
SOUND = False

system = os.uname()[0]

if system == "Linux":
    ROOT = "./chromedriver97"
else:
    ROOT = "./chromedriver97.exe"

def ashu():
    onlineclassscript("Ashu", "12016043", "ASHUahlawat@12",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN,sound=SOUND)
def ankit():
    onlineclassscript("Ankit", "12018329", "Gaara#29",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN)
# def gaurav():
#     onlineclassscript("Gaurav", "12014917", "Patel652002#",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN,sound=SOUND)
def sarthak():
    onlineclassscript("Sarthak", "12018433", "wq5uzG@#",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN,sound=SOUND)
def shrayansh():
	onlineclassscript("Shrayanh", "12016074", "#XMh@hWZ7$9s5r8",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN,sound=SOUND)


if "help" in PEOPLE:
    print("---------Welcome to ClassScript---------")
    print("Follow the steps to attend class:")
    help_man = '''(1)Open you class script folder in terminal.
                  (2)now run python3 or python all.py args
                  (3) arguments are :
                   -ankit,ashu,sarthak,swaksh,gaurav,shrayansh,rishika and  help for This page'''
    print(help_man)
    quit()

print("Selected people are:")

if "ashu" in PEOPLE :
    ashu_class = threading.Thread(target=ashu)
    ashu_class.start()
    print("Ashu")

if "ankit" in PEOPLE :
    ankit_class = threading.Thread(target=ankit)
    ankit_class.start()
    print("Ankit")

# if "gaurav" in PEOPLE :
#     gaurav_class = threading.Thread(target=gaurav)
#     gaurav_class.start()
#     print("Gaurav")

if "sarthak" in PEOPLE :
    sarthak_class = threading.Thread(target=sarthak)
    sarthak_class.start()
    print("Sarthak")
    
if "shrayansh" in PEOPLE :
    shrayansh_class = threading.Thread(target=shrayansh)
    shrayansh_class.start()
    print("Shrayansh")


