from time import sleep
import picking
#doc : https://gpiozero.readthedocs.io/en/latest/index.html

while(True):
    for i in range(7):
        picking.pick(i)
        sleep(0.5)
    sleep(2)

