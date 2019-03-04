import picking, time

while True:
    s = input("please enter a value between 0-5 (6 for exit)")
    try: 
        s = int(s)
        if s == 6:
            break
        else:
            picking.pick(s)

    except:
        print("not a valid number")
