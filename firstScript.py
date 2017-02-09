from datetime import datetime
import time

userName = "William"

def greet():
    print "Hello %s!!!" % userName
    print "The time is currently " + str(datetime.now())
    time.sleep(2)
    print "I hope this helps!!!"

greet()