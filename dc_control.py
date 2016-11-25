import RPi.GPIO as GPIO
from time import sleep

PIN1=29
PIN2=31
PIN3=33
PIN4=35

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(PIN3, GPIO.OUT)
GPIO.setup(PIN4, GPIO.OUT)

def go_forward(sec):
    GPIO.output(PIN1, GPIO.HIGH)
    GPIO.output(PIN4, GPIO.HIGH)
    sleep(sec)
    GPIO.output(PIN1, GPIO.LOW)
    GPIO.output(PIN4, GPIO.LOW)

def go_backward(sec):
    GPIO.output(PIN2, GPIO.HIGH)
    GPIO.output(PIN3, GPIO.HIGH)
    sleep(sec)
    GPIO.output(PIN2, GPIO.LOW)
    GPIO.output(PIN3, GPIO.LOW)

def turn_left(sec):
    GPIO.output(PIN1, GPIO.HIGH)
    GPIO.output(PIN3, GPIO.HIGH)
    sleep(sec)
    GPIO.output(PIN1, GPIO.LOW)
    GPIO.output(PIN3, GPIO.LOW)

def turn_right(sec):
    GPIO.output(PIN2, GPIO.HIGH)
    GPIO.output(PIN4, GPIO.HIGH)
    sleep(sec)
    GPIO.output(PIN2, GPIO.LOW)
    GPIO.output(PIN4, GPIO.LOW)

go_forward(1)
go_backward(1)
turn_left(1)
turn_right(1)

GPIO.cleanup()

