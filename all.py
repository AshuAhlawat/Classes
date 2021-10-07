people = ['ankit', 'ashu', 'gaurav', 'rishika', 'sarthak', 'shrayansh', 'swaksh']


import threading

def ankit():
    import ankit
def ashu():
    import ashu
def gaurav():
    import gaurav
def rishika():
    import rishika
def sarthak():
    import sarthak
def shrayansh():
	import shrayansh
def swaksh():
    import swaksh

ankit_class = threading.Thread(target=ankit)
ashu_class = threading.Thread(target=ashu)
gaurav_class = threading.Thread(target=gaurav)
rishika_class = threading.Thread(target=rishika)
sarthak_class = threading.Thread(target=sarthak)
shrayansh_class = threading.Thread(target=shrayansh)
swaksh_class = threading.Thread(target=swaksh)

if "ankit" in people:
    ankit_class.start()

if "ashu" in people:
    ashu_class.start()

if "gaurav" in people:
    gaurav_class.start()

if "rishika" in people:
    rishika_class.start()

if "sarthak" in people:
    sarthak_class.start()
    
if "shrayansh" in people:
    shrayansh_class.start()

if "swaksh" in people:
    swaksh_class.start()
