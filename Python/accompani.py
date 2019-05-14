import mxml_parse as mxml
import musthe as theory
import random
import xml.etree.ElementTree as ET
import os,sys

major_chords = ['M', 'm', 'm', 'M', 'M', 'm', 'm']
minor_chords = ['m', 'dim', 'M', 'm', 'M', 'M', 'M']

matrix = {\
1: [.5, 0, 0, .15, .35, 0, 0],\
2: [.2, .5, 0, 0, .3, 0, 0],\
3: [.4, 0, .5, 0, 0, .1, 0],\
4: [.2, .1, 0, .5, .2, 0, 0],\
5: [.4, 0, 0, .1, .5, 0, .0],\
6: [0, .3, 0, 0, .2, .5, 0],\
7: [.8, 0, 0, 0, .2, 0, 0]\
}

def get_chord_in_scale(idx, key):

	scale = theory.Scale(key[0], key[1])

	root = scale[(idx-1)%7]

	if key[1] == 'major':
		#return theory.Chord(root, major_chords[idx-1])
		return idx

	if key[1] == 'harmonic_minor':
		#return theory.Chord(root, minor_chords[idx-1])
		return idx

def get_scale_idx(note, key):

	scale = theory.Scale(key[0], key[1])

	for i in range(7):
		if scale[i].__eq__(theory.Note(note)):
			return i + 1

	raise ValueError("note not in scale")

def build_chord(num, key):

	scale = theory.Scale(key[0], key[1])
	letter = scale[num-1]

	if key[1] == 'major':
		ending = major_chords[num-1]

	if key[1] == 'minor':
		ending = minor_chords[num-1]

	print "letter is ", letter
	print "ending is ", ending
	return str(letter)+ending

def get_chord_options(note, key):

	scale = theory.Scale(theory.Note(key[0]), key[1])

	scale_idx_1 = get_scale_idx(note, key)
	scale_idx_2 = scale_idx_1 - 2
	scale_idx_3 = scale_idx_1 - 4

	options = [scale_idx_1, scale_idx_2, scale_idx_3]

	for i in range(len(options)):
		if options[i] <= 0:
			options[i] += 7

	print "chord options are ", sorted(options)
	return sorted(options)

def get_first_chord(first_note, key):
	options = get_chord_options(first_note, key)
	if key[0] in options:
		return build_chord(key[0], key)

	return build_chord(options[0], key)

#print get_first_chord('C', ('C', 'major'))

def get_next_chord(next_note, prev_chord, key):

	prev_chord_num = get_scale_idx(prev_chord[0], key)

	options = get_chord_options(next_note, key)
	print "options are ", options

	rand = random.seed()
	r = random.randint(1, 100) / float(100)

	if key[1] == 'major':
		probs = matrix[prev_chord_num]
		print "probs are ", probs
	if key[1] == 'harmonic_minor':
		probs = matrix[prev_chord_num]

	options_probs = []
	for i in range(7):
		if i+1 in options:
			prob = probs[i]
			options_probs.append(prob)

	s = sum(options_probs)
	normalized = [prob/s for prob in options_probs]

	print "normalized is ", normalized

	total = 0
	index = -1
	for i in range(0, len(normalized)):
		if r <= total + normalized[i]:
			index = i
			break
		total += normalized[i]

	return build_chord(options[index], key)

def get_all_chords(notes, key):
	first_note = notes[0]
	first_chord = get_first_chord(first_note, key)

	all_chords = [first_chord]

	prev_chord = first_chord
	for note in notes[1:]:
		next_chord = get_next_chord(note, prev_chord, key)
		all_chords.append(next_chord)
		prev_chord = next_chord

	return all_chords

def write_chords(all_chords, path):
	tree = ET.parse(path)
	root = tree.getroot()
	P1 = root.find('part')

	chord_counter = 0
	measure_counter = 0 #to find measure index to feed to add_chord
	for measure in P1.findall('measure'):
		for note in measure.findall('note'):
			note_index = measure.getchildren().index(note)
			if len(note.findall('pitch')) != 0:
				curr_chord = all_chords[chord_counter]

				if 'M' in curr_chord:
					mxml.add_chord(curr_chord[0:-1], 'major', measure_counter, note_index, tree)

				elif 'm' in curr_chord:
					mxml.add_chord(curr_chord[0:-1], 'minor', measure_counter, note_index, tree)

				elif 'dim' in curr_chord:
					mxml.add_chord(curr_chord[0:-3], 'diminished', measure_counter, note_index, tree)

				chord_counter += 1
		measure_counter += 1

def main():

	path = sys.argv[1]
	key_name = sys.argv[2]
	# key_name = 'C'
	key_tonality = sys.argv[3]
	# key_tonality = 'major'
	write_chords(get_all_chords(mxml.get_notes(path), (key_name, key_tonality)), path)

main()
#print get_all_chords(['C','D', 'E', 'D', 'C'], ('C', 'major'))
#write_chords(get_all_chords(mxml.get_notes('frenchsong.xml'), ('C', 'major')), 'frenchsong.xml')
