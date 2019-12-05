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

def getSongs(dir=""):
	#getting midis in repo
	if dir == ""
		mypath = getcwd()[:-15] + "music/"
	else:
		mypath = dir
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	validSongs = []
	for i in range(len(onlyfiles)):
		if onlyfiles[i][len(onlyfiles[i])-4:] == ".mid": #for each file, if substring of filename 4 chars from the end is '.mid'
			validSongs.append(onlyfiles[i]) #then the file is a midi file, and it's a song name
	return validSongs

def pickSong(validSongs):
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
			return chosenSong
		print("Invalid song \n")