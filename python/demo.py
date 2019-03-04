import picking, time

while True:
    s = input("please enter a value between 1-6 (0 for exit)")
    try: 
        s = int(s)
        if s == 0:
            break
        else:
            picking.pick(s)

    except:
        print("not a valid number")
