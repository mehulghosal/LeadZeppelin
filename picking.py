import gpiozero as gpio

#max and min
MAXANGLE = 7.5
MINANGLE = -7.5

STRUMMAXANGLE = 15
STRUMMINANGLE = -15

#pin numbers are temporary - change as needed
#angle values are temporary - change as needed

#INIT SERVOS
#index 0 is strummer servo
#indices 1-6 are indiv strings high to low
servos = [gpio.AngularServo(21, initial_angle=0, min_angle= STRUMMINANGLE, max_angle=STRUMMAXANGLE), gpio.AngularServo(20, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE), gpio.AngularServo(4, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE), gpio.AngularServo(5, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE), gpio.AngularServo(6, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE), gpio.AngularServo(7, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE), gpio.AngularServo(8, initial_angle=0, min_angle=MINANGLE, max_angle=MAXANGLE)]
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
    #Strumming
    if string == 0:
        if s == STRUMMAXANGLE:
            ang = STRUMMINANGLE
        elif s == STRUMMINANGLE:
            ang = STRUMMAXANGLE
    #Indiv strings
    else:
        if s == MAXANGLE:
            ang = MINANGLE
        elif s == MINANGLE:
            ang = MAXANGLE

    servos[string].angle = ang
    return ang
