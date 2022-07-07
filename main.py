RECORD = {

    #  Note: You passwords and Reg no are completely safe if you have any doubts just dont fking use it then.

    # str("you name alias here") : [int(reg. no here) , str("password here")]
}

art = """
--------------------------------------------------------------------
                            Welcome!                          
--------------------------------------------------------------------
Report Issues or Contribute: https://github.com/AshuAhlawat/Classes

Developers: Ashwani Ahlawat-(https://github.com/AshuAhlawat)
            Ankit Kumar-(https://github.com/Anky209e)
---------------------------------------------------------------------
Note: Always keep your code and chrome browser updated!
---------------------------------------------------------------------         
"""
print(art)
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


ROOT = "./chromedriver.exe"

try:
    os.uname()
    ROOT = "./chromedriver"
except:
    pass

if "help" in PEOPLE:

    help_man = '''
    ---------Welcome to ClassScript---------
    Follow the steps to attend class:
    (1)Open you class script folder in terminal.
    (2)now run python3 or python all.py args
    (3) arguments are :
                   the names added in RECORD
    
    '''
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
    quit()