import mido
from mido import MidiFile
mid = MidiFile('Bach_My_Heart_Ever_Faithful_BWV34.mid')

def noteSwitch(noteName):
	#60 = C4
	#notes are from 0-127 ()
	#midi can somehow play a C(-1), below C0. Do not be alarmed
	octave = -1
	while True:
		if noteName - 12 >= 0:
			noteName -= 12
			octave += 1
		else:
			break

	switcher = {
    	0: "C",
        1: "C#/Db",
        2: "D",
        3: "D#/Eb",
        4: "E",
        5: "F",
        6: "F#/Gb",
        7: "G",
        8: "G#/Ab",
        9: "A",
        10: "A#/Bb",
        11: "B"
    }
    if octave == 2:
    	if noteName < 4:
    		return "Cannot be played with normal guitar tuning"
    elif octave < 2:
    	return "Cannot be played with normal guitar tuning"
	return switcher[noteName] + str(octave)

for i, track in enumerate(mid.tracks):
	print('Track {}: {}'.format(i, track.name))
	for msg in track:
		m = str(msg)
		if msg.type == 'set_tempo':
			indexOfTempo = m.index("tempo=",0)+6
			indexOfSpace = m.index(" ",indexOfTempo)+0
			tempo = m[indexOfTempo:indexOfSpace]
			print("New tempo: " + str(tempo))
		elif msg.type == "note_on":
			indexOfNote = m.index("note=",0)+5
			indexOfSpace = m.index(" ",indexOfNote)+0
			note = m[indexOfNote:indexOfSpace]
			print("New note: " + str(noteSwitch(int(note))))