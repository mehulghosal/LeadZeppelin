from mido import MidiFile
mid = MidiFile('Bach_My_Heart_Ever_Faithful_BWV34.mid')
for i, track in enumerate(mid.tracks):
  print('Track {}: {}'.format(i, track.name))
  for msg in track:
    print(msg)
