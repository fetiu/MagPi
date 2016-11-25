import RPi.GPIO as GPIO
import curses
from curses import endwin

stdscr = curses.initscr()

curses.cbreak()
stdscr.keypad(True)

GPIO.setmode(GPIO.BOARD)
servoPin = 13
servoPin_2 = 11
GPIO.setup(servoPin,GPIO.OUT)
GPIO.setup(servoPin_2,GPIO.OUT)
pan_pwm=GPIO.PWM(servoPin,50)
tilt_pwm=GPIO.PWM(servoPin_2,50)

key=''
pan_degree = 90
tilt_degree = 90

pan_pwm.start(7)
tilt_pwm.start(7)
while key!=ord('q'):
    key = stdscr.getch()
    if key == curses.KEY_UP:
        if not tilt_degree==0:
            tilt_degree -= 1
        print(tilt_degree)
    elif key == curses.KEY_DOWN:
        if not tilt_degree==180:
            tilt_degree += 1
        print(tilt_degree)
    elif key == curses.KEY_LEFT:
        if not pan_degree==0:
            pan_degree -= 1
        print(pan_degree)
    elif key == curses.KEY_RIGHT:
        if not pan_degree==180:
            pan_degree += 1
        print(pan_degree)
    pan_pwm.ChangeDutyCycle(1./18.*pan_degree+2)
    tilt_pwm.ChangeDutyCycle(1./18.*tilt_degree+2)
    #stdscr.clear()
curses.endwin()
pan_pwm.stop()
tilt_pwm.stop()
GPIO.cleanup()


