from mido import MidiFile
mid = MidiFile('Bach_My_Heart_Ever_Faithful_BWV34.mid')
for i, track in enumerate(mid.tracks):
  print('Track {}: {}'.format(i, track.name))
  for msg in track:
  	m = str(msg)
    if "set_tempo" in m:
    	strAfterTempo = m.str(m.index("tempo=",0))
    	print(strAfterTempo);
    elif "note_on" in m:
    	print(m);