import picking, time

while True:
    s = int(input("please enter a value between 0-5 (6 for exit)"))
    if s == 6:
        break
    else:
        picking.pick(s)
