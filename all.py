PEOPLE = ['ankit','ashu']
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
    onlineclassscript("Ashu", "12016043", "ASHUahlawat@12",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN)
def swaksh():
    onlineclassscript("Swaksh", "12015939", "Sandyruby@12",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN)
def ankit():
    onlineclassscript("Ankit", "12018329", "Gaara#29",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN)
def gaurav():
    onlineclassscript("Gaurav", "12014917", "Patel652002#",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN)
def sarthak():
    onlineclassscript("Sarthak", "12018433", "wq5uzG@#",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN)
def shrayansh():
	onlineclassscript("Shrayanh", "12016074", "#XMh@hWZ7$9s5r8",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN)
def rishika():
    onlineclassscript("Rishika", "12018291", "Rishi@270",ROOT,method=METHOD,mute=MUTE,noscreen=NO_SCREEN)


ashu_class = threading.Thread(target=ashu)
swaksh_class = threading.Thread(target=swaksh)
ankit_class = threading.Thread(target=ankit)
gaurav_class = threading.Thread(target=gaurav)
sarthak_class = threading.Thread(target=sarthak)
shrayansh_class = threading.Thread(target=shrayansh)
rishika_class = threading.Thread(target=rishika)


if "ashu" in PEOPLE:
    ashu_class.start()

if "swaksh" in PEOPLE:
    swaksh_class.start()

if "ankit" in PEOPLE:
    ankit_class.start()

if "gaurav" in PEOPLE:
    gaurav_class.start()

if "sarthak" in PEOPLE:
    sarthak_class.start()
    
if "shrayansh" in PEOPLE:
    shrayansh_class.start()

if "rishika" in PEOPLE:
    rishika_class.start()
