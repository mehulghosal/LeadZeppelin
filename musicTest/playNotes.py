from os import listdir
from os.path import isfile, join
from parseMidi import parse

#figuring out what valid songs are
mypath = "C:\\Users\\22barkera\\LeadZeppelin\\musicTest"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
validSongs = []
for i in range(len(onlyfiles)):
	if onlyfiles[i][len(onlyfiles[i])-4:] == ".mid":#for each file, if substring of filename 4 chars from the end is '.mid'
		validSongs.append(onlyfiles[i])#then the file is a midi file, and it's a song name

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
returnedStuff = parse(chosenSong)#returns a tuple, consisting of an array of tuples, and an array of array of arrays of tuples
tempoChanges = returnedStuff[0]
chords = returnedStuff[1]
for s in range(len(tempoChanges)):
	#do stuff
for s in range(len(returnedStuff)):
	#even more stuff