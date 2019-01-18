import mido
from mido import MidiFile

def calcOctave(noteName):
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

	# switcher = {
 #    	0: "C",
 #        1: "C#/Db",
 #        2: "D",
 #        3: "D#/Eb",
 #        4: "E",
 #        5: "F",
 #        6: "F#/Gb",
 #        7: "G",
 #        8: "G#/Ab",
 #        9: "A",
 #        10: "A#/Bb",
 #        11: "B"
 #    }
	if octave == 2:
		if noteName < 4:
			return "Cannot be played with normal guitar tuning"
	elif octave < 2:
		return "Cannot be played with normal guitar tuning"
	return (noteName, octave)

def parse(midiName):
	mid = MidiFile(midiName)

	chords = []#to hold all the chords
	chordNotes = []#to track the notes parsed. example list: [(4,1),(7,1),("time",120)] -> play E1 & G1 for 120ms
	tempoChanges = []

	firstOn = False
	firstOff = True
	for i, track in enumerate(mid.tracks):
		for msg in track:
			m = str(msg)
			if msg.type == "set_tempo":
				indexOfTempo = m.index("tempo=",0)+6
				indexOfSpace = m.index(" ",indexOfTempo)
				tempo = m[indexOfTempo:indexOfSpace]
				indexOfTime = m.index("time=",0)+5
				indexOfGTS = m.index(">",0)#GTS = greater-than sign or '>'
				time = m[indexOfTime:indexOfGTS]
				
				tempoChanges.append((int(tempo),int(time)))
			else:
				if msg.type == "note_on":
					if firstOn == True and chordNotes:#all notes in previous chord have been turned on & off, so new chord.
						chord = []
						chord.extend(chordNotes)
						chords.append(chord)#add the 'packaged' chord to the chords
						chordNotes.clear()
						firstOn = False

					indexOfNote = m.index("note=",0)+5
					indexOfSpace = m.index(" ",indexOfNote)
					note = m[indexOfNote:indexOfSpace]
					chordNotes.append(calcOctave(int(note)))

					firstOff = True
				elif msg.type == "note_off":
					if firstOff == True:
						indexOfTime = m.index("time=",0)+5
						time = m[indexOfTime:]
						chordNotes.append(("time",int(time)))

						firstOff = False
						firstOn = True
	return chords