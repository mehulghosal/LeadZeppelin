print()
print("Fibonacci Sequence")
n = int(input("Enter n for how many times you want add the preceding numbers. n = "))
a = 0
b = 1
count = 0
max_count = n
while count < max_count:
	count = count + 1
	a2 = a
	b2 = b
	a = b2
	b = a2 + b2
	print(a2)