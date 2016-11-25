import os
import sys
from time import sleep
import curses

os.system('sudo /etc/init.d/servoblaster start')
stdscr=curses.initscr()
curses.cbreak()
stdscr.keypad(True)
class servo:
    def __init__(self,num,val):
        self.num=num
        self.val=val
        self._initVal__=val
        self.command='echo '+str(self.num)+'='+str(self.val)+' > /dev/servoblaster'
        os.system(self.command)

    def reset(self):
        self.val=self._initVal__
        self.command='echo '+str(self.num)+'='+str(self.val)+' > /dev/servoblaster'
        os.system(self.command)
        
    def move_plus(self,d):
        if self.val<250:
            self.val= self.val+d
        else:
            self.val=250
        self.command='echo '+str(self.num)+'='+str(self.val)+' > /dev/servoblaster'
        print(self.command)
        
    def move_minus(self,d):
        if self.val>50:
            self.val= self.val-d
        else:
            self.val=50
        self.command='echo '+str(self.num)+'='+str(self.val)+' > /dev/servoblaster'
        print(self.command)

pan_sv = servo(1,150)#servo1, init value is 150
tilt_sv= servo(2,250)#servo2, init value is 250

key=''
diff=1
prev='none'

while not key == ord('q'):
    key = stdscr.getch()
    if key==prev:
        diff+=1
    else:
        diff=1

    if key==curses.KEY_UP:
        tilt_sv.move_minus(diff)
    elif key== curses.KEY_DOWN:
        tilt_sv.move_plus(diff)
    elif key== curses.KEY_LEFT:
        pan_sv.move_plus(diff)
    elif key== curses.KEY_RIGHT:
        pan_sv.move_minus(diff)
    elif key== ord('r'):
        pan_sv.reset()
        tilt_sv.reset()
    prev=key
    os.system(pan_sv.command)
    os.system(tilt_sv.command)
    sleep(0.02)
curses.endwin()
os.system('sudo /etc/init.d/servoblaster stop')

