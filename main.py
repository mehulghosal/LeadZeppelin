from picking import pick

#takes in keyboard intakes (0-6)
def play():
	while True:
		try:
			inp = int(input("enter number for string (0 for strum): "))
			pick(inp)
		except Exception:
			continue
		

if __name__ == 'main':
	play()