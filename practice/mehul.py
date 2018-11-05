def fizzbuzz():
	for i in range(100):
		output = ""
		if i%3==0:
			output += "fizz"
		if i%5==0:
			output += "buzz"

		if output == "":
			output += str(i)

		print(output)

def primes():
	n = int(input("enter upper bound: "))
	if n <=1: 
		print("invalid upper bound")
	else:
		for i in range(2, n):
			for j in range(2, i):
				i%j==0:
					