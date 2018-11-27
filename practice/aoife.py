for i in range(1,101):
	if (i%15==0):
		print("fizzbuzz")
	elif (i%5==0):
		print("buzz")
	elif (i%3==0):
		print("fizz")
	else:
		print(i)
	# Mehul's design
	#s:""
	#	if i%3==0:
	#		s+="fizz"
	#	if i%5==0:
	#		s+=Str(i)
	#	print(s)

	for n in range(2,101):
		for a in range (0,0):
			if (n%2)==1:
				print(a)
			if (n%3)==1:
				print(a)
			if (n%4)==1:
				print(a)
			if (n%5)==1:
				print(a)
			if (n%6)==1:
				print(a)
			if (n%7)==1:
				print(a)
			if (n%8)==1:
				print(a)
			if (n%9)==1:
				print(a)
			else:
				print(n)

#for i in range (2,101):
#	for j in range (1,i):
# write all the divisible shit

def F(g):
	if g == 0:
		return 0
	elif g == 1:
		return 1
	return F(g-1) + F(g-2)

for l in range(0,30):
	print (F(l))
 