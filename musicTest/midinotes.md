# Notes on Midi

* using mido - python library
* http://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
* https://mido.readthedocs.io/en/latest/midi_files.html
* for now, ignore control changes and meta messages
* note on plays a note, note off turns it off
* note parameter in note message is the pitch: 60 = middle C, one integer step is half tone
* time is the delta time in ticks: "ticks_per_beat in MidiFile objects"

to do:
* u guys can individually learn how to read in a text file 
* parse test.txt and deal with music shit - refer to notes abv
* we're only really looking at the noteon/off messages
* handle delta time and pitches