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

import parseMidi as midi

guitarStrings = [[],[],[],[],[],[]] #will contain all possible notes on each string

chords = [] #holds parsed chords
tempoChanges = [] #holds parse tempo changes

railPos = [ [10,10,10,10,10,10,0] ] #starting positions of each of the pushers (10 is arbitrary right now)
									#list in a list because holds other rail positions
pickStrings = [] #holds which strings are picked each chord

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
	possibleStrings = {}
	for i in range(6):
		if noteTuple in guitarStrings[i]:
			possibleStrings[i] = guitarStrings[i].index(noteTuple) #add a tuple with which string and the note's position on it
	return possibleStrings

def getMusic(chosenSong):
	returnedStuff = midi.parse(chosenSong) #returns a tuple, consisting of an array of tuples, and an array of arrays of tuples
	tempoChanges = returnedStuff[0]
	chords = returnedStuff[1]
	for c in chords: #example: [(0, 4), (9, 3), 120]
		availableStrings = [0,1,2,3,4,5] #strings that can be played, 0 lowest 5 is highest
		stringsToPick = [] #to tell which strings to be picked
		newRailPos = []
		for t in reversed(range(len(c)-1)): #for each tuple item, excluding the time, backwards.
											#this is because the parseMidi formats the notes highest first, and
											#lowest must be prioritized. Therefore, last note before the time value
											#is the lowest note, and start there

			rawPosStrings = checkNote(c[t]) #checks which strings the note can be played on
			relativeDist = {}
			for k, v in rawPosStrings.items(): #for each string(k), fret(v) in all possible string positions
				if k in availableStrings: #string isn't playing another note
					if v == 0: #prioritizing open string
						relativeDist[k] = -1 #so it's better to do open than playing the same note
					else:
						mostRecentRailPositions = railPos[len(railPos)-1] #the latest rail positions
						posOfString = mostRecentRailPositions[k] #get the position of pusher on string k
						relativeDist[k] = abs(v - positionOfString) #distance from pusher to note's fret

			lowestString = min(relativeDist, key=relativeDist.get) #string with lowest distance
			lowestPos = rawPosStrings.get(lowestString) #actual lowest position
			newRailPos.append()
			availableStrings.remove(lowestString) #the string is going to be playing a note
			stringsToPick.append(lowestString) #pick the string
		newRailPos.append(c.get(len(c)-1)) #append the time of the chord
		railPos.append(newRailPos) #put the new rail position into list of all of them
		pickStrings.append(stringsToPick) #put the strings to be picked in the list

def getPickStrings():
	return chords

def getRailPos(tuning):
	return railPos
