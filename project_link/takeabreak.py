#this is a script to remind me to take a break/stand up

import time
import webbrowser
import os

total_breaks = 7
break_count = 0

while(break_count<total_breaks):
    time.sleep(2700)
    webbrowser.get('Safari').open('https://randomgoat.com/')
    time.sleep(18)
    os.system("killall -9 'Safari'")
    break_count += 1


#https://blog.udacity.com/2015/01/remind-friend-take-break-python-program.html
#https://stackoverflow.com/questions/42568922/how-to-close-web-browser-using-python
