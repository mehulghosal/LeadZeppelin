import mido
from mido import MidiFile
mid = MidiFile('Bach_My_Heart_Ever_Faithful_BWV34.mid')
for i, track in enumerate(mid.tracks):
	print('Track {}: {}'.format(i, track.name))
	for msg in track:
		m = "a"
		m = str(msg)
		if msg.type == 'set_tempo':
			indexOfTempo = m.index("tempo=",0)+6
			indexOfSpace = m.index(" ",indexOfTempo)+0
			tempo = m[indexOfTempo:indexOfSpace]
			print(tempo)
		#elif msg.type == "note_on":
			#print(m)