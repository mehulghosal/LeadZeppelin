#with standard guitar tuning, you can play E2-B5

# 0: "C",
# 1: "C#/Db",
# 2: "D",
# 3: "D#/Eb",
# 4: "E",
# 5: "F",
# 6: "F#/Gb",
# 7: "G",
# 8: "G#/Ab",
# 9: "A",
# 10: "A#/Bb",
# 11: "B"

guitarStrings = [[],[],[],[],[],[]] #6 empty arrays that will contain notes that can be played on each string

def tune(tuning = [(4,2), (10,2), (2,3), (7,3), (11,3), (4,4)]): #sets default tuning strings
	for i in range(6):
		noteCounter = tuning[i][0]
		octaveCounter = tuning[i][1]
		for j in range(20): #20 playable notes, including open string
			guitarStrings[i].append((noteCounter, octaveCounter))
			noteCounter += 1
			if noteCounter == 12:
				noteCounter = 0
				octaveCounter += 1

def checkNote(noteTuple):
	possibleStrings = []
	for i in range(6):
		if noteTuple in guitarStrings[i]:
			possibleStrings.append( (i,guitarStrings[i].index(noteTuple)) ) #add a tuple with which string and the note's position on it
	return possibleStrings