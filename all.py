people = ['ankit','ashu','swaksh']


import threading

def ashu():
    import ashu
def swaksh():
    import swaksh
def ankit():
    import ankit
def gaurav():
    import gaurav
def sarthak():
    import sarthak
def shrayansh():
	import shrayansh


ashu_class = threading.Thread(target=ashu)
swaksh_class = threading.Thread(target=swaksh)
ankit_class = threading.Thread(target=ankit)
gaurav_class = threading.Thread(target=gaurav)
sarthak_class = threading.Thread(target=sarthak)
shrayansh_class = threading.Thread(target=shrayansh)


if "ashu" in people:
    ashu_class.start()

if "swaksh" in people:
    swaksh_class.start()

if "ankit" in people:
    ankit_class.start()

if "gaurav" in people:
    gaurav_class.start()

if "sarthak" in people:
    sarthak_class.start()
    
if "shrayansh" in people:
    shrayansh_class.start()
