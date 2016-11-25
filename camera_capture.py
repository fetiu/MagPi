from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1280,720)
camera.rotation = 180

#camera.start_preview()
while True:
    camera.capture('/home/pi/my_python/images/tmp/stream.jpg')
    sleep(0.03)
