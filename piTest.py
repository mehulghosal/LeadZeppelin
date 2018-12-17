import time

#doc : https://gpiozero.readthedocs.io/en/latest/index.html
import gpiozero as gpio

s = gpio.AngularServo(2, min_angle = 0, max_angle = 180)
while(True):
    s.min()
    time.sleep(3)
    s.max()
    time.sleep(3)