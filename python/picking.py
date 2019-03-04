import gpiozero as gpio

#max and min
MAXANGLE = 1
MINANGLE = -1

#pin numbers are temporary - change as needed
#angle values are temporary - change as needed

#INIT SERVOS

servos = [gpio.AngularServo(21, initial_angle=0, min_angle= MINANGLE, max_angle=MAXANGLE), gpio.AngularServo(20, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE), gpio.AngularServo(4, initial_angle=0, min_angle=60, max_angle=90), gpio.AngularServo(5, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE), gpio.AngularServo(6, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE), gpio.AngularServo(12, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE)]
for i in servos: i.min()

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
    ang = 0
    #Indiv strings
    if s == servos[string].max_angle:
        servos[string].min()
    elif s == servos[string].min_angle:
        servos[string].max()

    return ang

