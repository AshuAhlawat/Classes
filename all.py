import sys
args_arr = sys.argv
PEOPLE = []
for i in args_arr:
    PEOPLE.append(i)
NO_SCREEN = True
MUTE = True
methods = ["Microphone","Listen only"]
METHOD = methods[0]


from script import onlineclassscript

import os
import threading

system = os.uname()[0]
if system == "Linux":
    ROOT = "./chromedriver94"
else:
    ROOT = "./chromedriver94.exe"
    NO_SCREEN=False


def ashu():
    onlineclassscript("Ashu", "12016043", "ASHUahlawat@12",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN,sound=True)
def swaksh():
    onlineclassscript("Swaksh", "12015939", "Sandyruby@12",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN,sound=True)
def ankit():
    onlineclassscript("Ankit", "12018329", "Gaara#29",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN)
def gaurav():
    onlineclassscript("Gaurav", "12014917", "Patel652002#",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN,sound=True)
def sarthak():
    onlineclassscript("Sarthak", "12018433", "wq5uzG@#",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN,sound=True)
def shrayansh():
	onlineclassscript("Shrayanh", "12016074", "#XMh@hWZ7$9s5r8",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN,sound=True)
def rishika():
    onlineclassscript("Rishika", "12018291", "Rishi@270",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN,sound=True)


ashu_class = threading.Thread(target=ashu)
swaksh_class = threading.Thread(target=swaksh)
ankit_class = threading.Thread(target=ankit)
gaurav_class = threading.Thread(target=gaurav)
sarthak_class = threading.Thread(target=sarthak)
shrayansh_class = threading.Thread(target=shrayansh)
rishika_class = threading.Thread(target=rishika)

print("Selected options are:")
for i in range(1,len(PEOPLE)):
    print("(*)"+PEOPLE[i])

if "ashu" in PEOPLE :
    ashu_class.start()

if "swaksh" in PEOPLE :
    swaksh_class.start()

if "ankit" in PEOPLE :
    ankit_class.start()

if "gaurav" in PEOPLE :
    gaurav_class.start()

if "sarthak" in PEOPLE :
    sarthak_class.start()
    
if "shrayansh" in PEOPLE :
    shrayansh_class.start()

if "rishika" in PEOPLE :
    rishika_class.start()
if "help" in PEOPLE:
    print("---------Welcome to ClassScript---------")
    print("Follow the steps to attend class:")
    help_man = '''(1)Open you class script folder in terminal.
                  (2)now run python3 or python all.py args
                  (3) arguments are :
                   -ankit,ashu,sarthak,swaksh,gaurav,shrayansh,rishika and  help for This page'''
    print(help_man)