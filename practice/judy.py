print()
print("First Problem: Fizz Buzz")
for i in range(1, 101):
	if i%3 != 0 and i%5 != 0:
		print(i)
	elif i%3 == 0 and i%5 == 0:
		print("FizzBuzz")
	elif i%3 == 0:
		print("Fizz")
	elif i%5 == 0:
		print("Buzz")
print("Yay. It worked.")
print()
print()
print()
print("Second Problem: Primes")
print("Welcome to the Sieve of Eratosthenes!")
n = int(input("Enter n for all prime numbers between 1 and n. n = "))
if n < 0:
	print("Please input a positive number.")
if n == 0:
	print("Why? Input something greater than 1.")
if n > 1:
	print("Here are your prime numbers!")
if n == 1:
	print("Something after 1. Also, 1 is not a prime number.")
if n > 2 or n == 2:
	print(2)
if n > 3 or n == 3:
	print(3)
if n > 5 or n == 5:
	print(5)
if n > 7 or n == 7:
	print(7)
for i in range(2, n+1):
	if i%2 != 0 and i%3 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0:
		print(i)