for i in range(1,101):
	if (i%15==0):
		print("fizzbuzz")
	elif (i%5==0):
		print("buzz")
	elif (i%3==0):
		print("fizz")
	elif (i%1==0):
		print(i)
	elif (i%2==0):
		print(i)
	elif (i%4==0):
		print(i)
	elif (i%6==0):
		print(i)
	elif (i%7==0):
		print(i)
	elif (i%8==0):
		print(i)
	elif (i%9==0):
		print(i)

num = int(input("Enter a number"))
if (num < 1):
	print("YouFudgedUpBro")
if (num > 1):
	for i in range (2,num):
		if (num % i) == 0:
			print (num, "ce n'est pas un prime number")	
			print (i, "times", num//i, "is", num)
	else:
		print(num, "ITS A PRIME NUMERO Senoritas")

