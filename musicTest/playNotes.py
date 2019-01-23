from os import listdir
from os.path import isfile, join
from parseMidi import parse

#figuring out what valid songs are
mypath = "C:\\Users\\22barkera\\LeadZeppelin\\musicTest"
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
	print(tempoChanges[s])

print("\n")

for s in range(len(chords)): #example: [(0, 4), (9, 3), 120]
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
	for i in range(len(chords[s])-1): #for each tuple excluding time
		pass
		#figure out which string to play the note, and where
			#the lowest note is the second-to-last tuple and goes backwards
			#the fretboard is 17in long, the exact middle is the metal fret between the 7th and 8th frets
			#we would want to play higher up the string if possible bc less movement to change pitch
	#add the time to wait at the end?
	print(chords[s])