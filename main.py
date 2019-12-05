import playNotes as play
import noteMapping as note

play.getSongs()
song = play.pickSong()

note.tune()
data = getMusic(song)
tempoChanges = data[0]
railPos = data[1]
pickStrings = data[2]

for i in range(len(pickStrings)):
	#wait railPos[i+1][6] ticks?
	
	#thread 1:
	for j in railPos[i+1]:
		pass
		#pusher 1 to position railPos[i+1][0]

	#thread 2:
	for k in pickStrings[i]: #find a way to pick them at the same time?
		pick(k)