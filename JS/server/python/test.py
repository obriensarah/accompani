import midi
#import numpy as np
import copy
import ast
import os

cwd = os.getcwd()
print("python directory is ", cwd)

#pattern = midi.read_midifile("../test_simple.mid")
#print(pattern)

'''p = midi.Pattern(format=0, resolution=480, tracks=\
[midi.Track(\
  [midi.TrackNameEvent(tick=0, text='Classic Electric Piano', data=[67, 108, 97, 115, 115, 105, 99, 32, 69, 108, 101, 99, 116, 114, 105, 99, 32, 80, 105, 97, 110, 111]),
   midi.InstrumentNameEvent(tick=0, text='Classic Electric Piano', data=[67, 108, 97, 115, 115, 105, 99, 32, 69, 108, 101, 99, 116, 114, 105, 99, 32, 80, 105, 97, 110, 111]),
   midi.TimeSignatureEvent(tick=0, data=[4, 2, 24, 8]),
   midi.KeySignatureEvent(tick=0, data=[0, 0]),
   midi.SmpteOffsetEvent(tick=0, data=[32, 0, 0, 0, 0]),
   midi.SetTempoEvent(tick=0, data=[7, 161, 32]),
   midi.NoteOnEvent(tick=88, channel=0, data=[48, 98]),
   midi.NoteOnEvent(tick=0, channel=0, data=[36, 90]),
   midi.NoteOnEvent(tick=0, channel=0, data=[40, 90]),
   midi.NoteOnEvent(tick=0, channel=0, data=[43, 90]),
   midi.NoteOnEvent(tick=513, channel=0, data=[50, 98]),
   midi.NoteOnEvent(tick=0, channel=0, data=[31, 90]),
   midi.NoteOnEvent(tick=0, channel=0, data=[35, 90]),
   midi.NoteOnEvent(tick=0, channel=0, data=[38, 90]),
   midi.NoteOffEvent(tick=22, channel=0, data=[48, 64]),
   midi.NoteOnEvent(tick=505, channel=0, data=[52, 98]),
   midi.NoteOffEvent(tick=17, channel=0, data=[50, 64]),
   midi.NoteOnEvent(tick=484, channel=0, data=[48, 98]),
   midi.NoteOffEvent(tick=27, channel=0, data=[52, 64]),
   midi.NoteOffEvent(tick=1919, channel=0, data=[48, 64]),
   midi.EndOfTrackEvent(tick=0, data=[])])])'''

#print(pattern[0][0])

#track = pattern[0]

'''t = track[-2]
print(t)
print(t.tick)
print(t.data)
print(t.channel)'''
#midi.write_midifile("test.mid", p)

def read_file(path):
	with open(path) as f:
		#file = open(path, "r")
		read = f.read().splitlines()
		midi_path = read[0]
		chords = read[1]

	chords = ast.literal_eval(chords)
	return chords, midi_path

def final(chords, path):
	pattern = midi.read_midifile(path)
	track = pattern[0]
	l = len(track)

	chord_counter = 0

	num_notes = []

	for i in range(l):
		if isinstance(track[i], midi.NoteOnEvent):
			num_notes.append(i)

	i = 0
	for index in num_notes:
		event1 = midi.NoteOnEvent(tick=0, channel=0, data=[chords[chord_counter][0], 60])
		event2 = midi.NoteOnEvent(tick=0, channel=0, data=[chords[chord_counter][1], 60])
		event3 = midi.NoteOnEvent(tick=0, channel=0, data=[chords[chord_counter][2], 60])
		track.insert(index + 1 + i, event1)
		track.insert(index + 2 + i, event2)
		track.insert(index + 3 + i, event3)
		i += 3

		chord_counter += 1


	off_indices = []
	for i in range(len(track)):
		if isinstance(track[i], midi.NoteOffEvent):
			off_indices.append(i)

	chord_counter = 0
	i = 0
	for index in off_indices:
		event1 = midi.NoteOffEvent(tick=0, channel=0, data=[chords[chord_counter][0], 60])
		event2 = midi.NoteOffEvent(tick=0, channel=0, data=[chords[chord_counter][1], 60])
		event3 = midi.NoteOffEvent(tick=0, channel=0, data=[chords[chord_counter][2], 60])
		track.insert(index + 1 + i, event1)
		track.insert(index + 2 + i, event2)
		track.insert(index + 3 + i, event3)
		i += 3

		chord_counter += 1

	'''track.insert(7, midi.NoteOnEvent(tick=0, channel=0, data=[36, 90]))'''
	print("writing pattern to harmoni.mid")
	# print("pattern is ", pattern)
	midi.write_midifile("harmoni.mid", pattern)


#write_midi([[36, 40, 43], [31, 35, 38], [36, 40, 43], [36, 40, 43]], "./test_simple.mid")
#test()
#test("test_simple.mid")
#final([[60,64,67], [67,71,74], [60,64,67],[60,64,67]], "test_simple.mid")

chords,path = read_file("java_out.txt")
#print(ast.literal_eval(chords))

final(chords, path)
