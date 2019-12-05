import gpiozero as gpio

#max and min
MAXANGLE = 1
MINANGLE = -1

#pin numbers are temporary - change as needed
#angle values are temporary - change as needed

#INIT SERVOS

servos = [gpio.AngularServo(21, initial_angle=-50), gpio.AngularServo(20, initial_angle=-12), gpio.AngularServo(4, initial_angle=90), gpio.AngularServo(5, initial_angle=-27), gpio.AngularServo(6, initial_angle=-19), gpio.AngularServo(12, initial_angle=-10)]

angles = [(-50,-26), (-35,-12), (50,90), (-45,-27), (-35,-19), (-45,-10)]


#returns list of angle values in order servos are defined
def state():
    s = []
    for i in servos:
        s.append(i.angle)
    return s

#param string of type integer is which string is to be picked 
#does gpio wait until completion? - if not, we have to manually add delays
#return angle servo is set to
def pick(string):
    s = state()[string]
    ang = angles[string]
    
    if s == ang[0]:
        servos[string].angle = ang[1]
    elif s == ang[1]:
        servos[string].angle = ang[0]


