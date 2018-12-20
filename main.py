from picking import pick

#takes in keyboard intakes (0-6)
def play():
	while True:
		inp = int(input("enter number for string (0 for strum): "))
		pick(inp)

if __name__ == 'main':
	play()