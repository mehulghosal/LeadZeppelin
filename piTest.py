import time

t = time.time()
print("hello world")

for i in range(5000):
	print(i)

print(time.time() - t)

import RPIO.GPIO as gpio
gpio.setmode(gpio.board)

servo = GPIO.PWM(12, 50)
servo.start()

try:
	while True:
		servo.changeDutyCycle(7.5)
		time.sleep(1)
		servo.changeDutyCycle(2.5)
		time.sleep(1)
except KeyboardInterrupt:
	servo.stop()
	GPIO.cleanup()