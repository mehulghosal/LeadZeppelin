import math

def fizzBuzz():
	for i in range(1, 101):
		finalStr = ""
		if i % 3 == 0:
			finalStr += "fizz"
		if i % 5 == 0:
			finalStr += "buzz"
		print(str(i) + "\t" + str(finalStr))

def isPrime(num):
	if num == 1:
		return True
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

def primes():
	n = input("What number should it go up to?\n")
	arr = []
	for i in range(1, n+1):
		if isPrime(i):
			arr.append(i)
	print("\n")
	print(arr)


def printBoard(arr):
	for i in arr:
		lineStr = ""
		for j in i:
			lineStr += str(j) + " "
		print(lineStr)


def isWinningBoard(arr, withChar):

	for j in range(0, 3):
		works = True
		for i in arr:
			if i[j] != withChar: works = False
		if works: return True

	for i in arr:
		works = True
		for j in i:
			if j != withChar: works = False
		if works: return True

	diagWorks = (True, True)
	for i in range(0, 3):
		if arr[i][i] != withChar: diagWorks = (False, diagWorks[1])
		if arr[i][2-i] != withChar: diagWorks = (diagWorks[0], False)
	if diagWorks[0] or diagWorks[1]: return True

	return False

def inputLocation(characterTurn, board):
	x = -1
	y = -1
	print("Please enter the possition of " + str(characterTurn))
	while True:
		try:
			x = input("row number:\t") - 1
			y = input("column number:\t") - 1
			if board[x][y] == "-":
				break
			print("\nPlease enter a valid point")
		except:
			print("\nPlease enter a valid point")
			continue
	print("\n")
	return (x, y)



def runGame():
	board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
	currentPlayer = False
	while True:
		print("The board currently looks like:")
		printBoard(board)
		print("")
		playerChar = "X" if currentPlayer else "O"
		newLocation = inputLocation(playerChar, board)
		board[newLocation[0]][newLocation[1]] = playerChar
		if isWinningBoard(board, playerChar):
			print("\nPlayer " + playerChar + " Won the game!!!") 
			print("the winning board Looks like: ")
			printBoard(board)
			break
		currentPlayer = not currentPlayer

if __name__ == '__main__':
	while True:
		print("which process do you want?")
		print("FizzBuzz \t(1)")
		print("Primes \t\t(2)")
		print("Tic Tac Toe \t(3)")
		print("None\t\t(4)")
		process = input("\n")
		if process == 1:
			fizzBuzz()
		if process == 2:
			primes()
		if process == 3:
			runGame()
		if process == 4:
			break
		print("\n\n")