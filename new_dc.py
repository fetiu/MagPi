import RPi.GPIO as GPIO
from time import sleep
import curses
from curses import endwin

stdscr = curses.initscr()

curses.cbreak()
stdscr.keypad(True)

PIN1=29
PIN2=31
PIN3=33
PIN4=35
ENCLK=23

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(PIN3, GPIO.OUT)
GPIO.setup(PIN4, GPIO.OUT)
GPIO.setup(ENCLK, GPIO.OUT)

pwm = GPIO.PWM(ENCLK, 50)
pwm.start(50)

class wheel:
    def __init__(self,pin1,pin2,name):
        self.pin1=pin1
        self.pin2=pin2
        self.name=name
        self.status='stop' #3 status

    def forward(self,speed)
        pwm.ChangeDutyCycle(speed)
        GPIO.output(self.pin1, True)
        GPIO.output(self.pin2, False)
        self.status='forward'
        print(self.name,self.status)

    def backward(self,speed)
        pwm.ChangeDutyCycle(speed)
        GPIO.output(self.pin1, False)
        GPIO.output(self.pin2, True)
        self.status='backward'
        print(self.name,self.status)

    def stop(self,speed)
        if speed<=40:
            self.status='stop'

        if self.status=='forward': #for smooth stop
            self.forward(speed)
        elif self.status=='backward':
            self.forward(speed)
        else:
            GPIO.output(self.pin1, False)
            GPIO.output(self.pin2, False)

left =wheel(PIN1,PIN2,'left_wheel')
right =wheel(PIN4,PIN3,'right_wheel')

key=''
speed=40
prev='none'

while not key == ord('q')
    key = stdscr.getch()
    
    if key==prev:
        if speed<100:
            speed+=1
    else:
        if speed>40:
            speed-=1

    if key==ord('w'):   #go forward
        left.forward(speed)
        right.forward(speed)
    elif key==ord('s'): #go backward
        left.backward(speed)
        right.backward(speed)
    elif key==ord('a')  #turn left
        left.backward(speed)
        right.forward(speed)
    elif key==ord('d')  #turm right
        left.forward(speed)
        right.backward(speed)
    else
        left.stop(speed)
        right.stop(speed)
    prev = key
    sleep(0.02)
curses.endwin()
pwm.stop()
GPIO.cleanup()

