def fizzbuzz():
	for i in range (1, 100):
		if (i % 3 == 0 and i % 5 == 0):
			print("fizzbuzz")
		elif i % 3 == 0:
			print("fizz")
		elif i % 5 == 0:
			print("buzz")
		else:
			print(i)

def prime():
	n = int(input("enter any number."))

	for i in range(2, n + 1):
		counter = 0
		for j in range(2, i):
			if i % j == 0:
				counter += 1
		if counter == 0:
			print(i)

prime()