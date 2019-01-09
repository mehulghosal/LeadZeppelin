import mido

fN = 'Bach_My_Heart_Ever_Faithful_BWV34.mid'
m = mido.MidiFile(fN)
f = open('test.txt', 'w')
TPB = m.ticks_per_beat

s = str(TPB) + '\n'
for i, track in enumerate(m.tracks):
	s+= str(i) + track.name + "\n"
	for msg in track:
		s += str(msg) + '\n'

f.write(s)
f.close()

