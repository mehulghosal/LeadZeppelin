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
print("Will do Part 2 later.")