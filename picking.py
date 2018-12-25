import gpiozero as gpio

#max and min
MAXANGLE = 45
MINANGLE = 0

STRUMAXANGLE = 90
STRUMINANGLE = -90

#pin numbers are temporary - change as needed
#angle values are temporary - change as needed

#INIT SERVOS
servos = [gpio.AngularServo(2, initial_angle=0, min_angle= STRUMINANGLE, max_angle=STRUMAXANGLE), gpio.AngularServo(3, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE), gpio.AngularServo(4, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE), gpio.AngularServo(5, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE), gpio.AngularServo(6, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE), gpio.AngularServo(7, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE), gpio.AngularServo(8, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE)]

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
#does gpio wait until completion? - if not, we have to manually add delays
def pick(string):
	state = state()
	if string == 0: strum()
	elif string == 1:
		if state[1] == MAXANGLE:
			s1.min()
		elif state[1] == MINANGLE:
			s1.max()
	elif string == 2:
		if state[2] == MAXANGLE:
			s2.min()
		elif state[2] == MINANGLE:
			s2.max()
	elif string == 3:
		if state[3] == MAXANGLE:
			s3.min()
		elif state[3] == MINANGLE:
			s3.max()
	elif string == 4:
		if state[4] == MAXANGLE:
			s4.min()
		elif state[4] == MINANGLE:
			s4.max()
	elif string == 5:
		if state[5] == MAXANGLE:
			s5.min()
		elif state[5] == MINANGLE:
			s5.max()
	elif string == 6:
		if state[6] == MAXANGLE:
			s6.min()
		elif state[6] == MINANGLE:
			s6.max()