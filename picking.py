import gpiozero as gpio

#max and min
MAXANGLE = 90
MINANGLE = -90

STRUMAXANGLE = 90
STRUMINANGLE = -90

#pin numbers are temporary - change as needed
#angle values are temporary - change as needed

#INIT SERVOS
strummer = gpio.AngularServo(2, initial_angle=0, min_angle= STRUMINANGLE, max_angle=STRUMAXANGLE)
s1 = gpio.AngularServo(3, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE)
s2 = gpio.AngularServo(4, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE)
s3 = gpio.AngularServo(5, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE)
s4 = gpio.AngularServo(6, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE)
s5 = gpio.AngularServo(7, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE)
s6 = gpio.AngularServo(8, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE)

#returns list of angle values in order servos are defined
def state():
	return [strummer.angle, s1.angle, s2.angle, s3.angle, s4.angle, s5.angle, s6.angle]

#strums across all strings
def strum():
	if state()[0] == strummer.max_angle:
		strummer = strummer.min_angle
	elif state()[0] == strummer.min_angle:
		strummer = strummer.max_angle

#param string of type integer is which string is to be picked 
def pick(string):
	state = state()
	if string == 1:
		if state[1] == MAXANGLE:
			s1.min()
		elif state[1] == MINANGLE:
			s1.max()
	elif string == 2:
		if state[2] == MAXANGLE:
			s2.min()
		elif state[2] == MINANGLE:
			s2.max()
	#repeat