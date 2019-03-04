from os import listdir, getcwd
from os.path import isfile, join
from parseMidi import parse
from noteMapping import tune, checkNote

distance = [
	0 #to play open string 0 distance
	#from middle of first fret to middle of second fret
	#from middle of second fret to middle of third fret
	#and so on
]

#figuring out what valid songs are
mypath = getcwd()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
validSongs = []
for i in range(len(onlyfiles)):
	if onlyfiles[i][len(onlyfiles[i])-4:] == ".mid": #for each file, if substring of filename 4 chars from the end is '.mid'
		validSongs.append(onlyfiles[i]) #then the file is a midi file, and it's a song name

#presenting the songs to the user
chosenSong = ""
while True:
	print("Song choices:")
	for i in range(len(validSongs)):
		print("\t" + str(i+1) + " " + validSongs[i] + "\n")
	print("Enter a number between 1 and " + str(len(validSongs)) + " to choose a song")
	ans = input()
	if int(ans) >= 1 and int(ans) <= len(validSongs):
		print("That's a valid song")
		chosenSong = validSongs[int(ans)-1]
		break
	print("Invalid song")

#doing stuff with the song
returnedStuff = parse(chosenSong) #returns a tuple, consisting of an array of tuples, and an array of arrays of tuples
tempoChanges = returnedStuff[0]
chords = returnedStuff[1]

for s in range(len(tempoChanges)): #example: (1363636, 52920)
	pass

tune() #if different tuning, put all six strings in argument array
railPos = [ [10,10,10,10,10,10,0] ] #starting positions of each of the pushers (10 is arbitrary right now)
pickStrings = []
for c in chords: #example: [(0, 4), (9, 3), 120]
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
	availableStrings = [0,1,2,3,4,5] #strings that can be played, 0 lowest 5 is highest
	stringsToPick = [] #to tell which strings to be pick ed
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
		lowestPos = relativeDist[lowestString] #actual lowest distance value
		availableStrings.remove(lowestString) #the string is going to be playing a note
		stringsToPick.append(lowestString) #pick the string
	railPos.append()
	pickStrings.append(stringsToPick)