import picking, time

print("enter a sequence of numbers")

arr = []
while True:
    inPut = input("\nnext: \n")
    if inPut == -1:
        break
    arr.append(inPut)

tim = input("Please enter the time interval (Seconds)")


count = 0
while True:
    time.sleep(tim)
    picking.pick(arr[count])
    count += 1
    if count >= len(arr):
        count = 0

