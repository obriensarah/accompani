import mxml_parse as mxml
import musthe as theory
import random
import xml.etree.ElementTree as ET
import os,sys
import dynamicMatrix

major_chords = ['M', 'm', 'm', 'M', 'M', 'm', 'dim']
minor_chords = ['m', 'm', 'M', 'm', 'm', 'M', 'M']

'''matrix = {\
1: [.5, 0, 0, .15, .35, 0, 0],\
2: [.2, .5, 0, 0, .3, 0, 0],\
3: [.4, 0, .5, 0, 0, .1, 0],\
4: [.2, .1, 0, .5, .2, 0, 0],\
5: [.4, 0, 0, .1, .5, 0, .0],\
6: [0, .3, 0, 0, .2, .5, 0],\
7: [.8, 0, 0, 0, .2, 0, 0]\
}'''
matrix = {}

def num_to_rn(num):
	rns = [None, 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii']
	return rns[num]

def rn_to_num(rn):
	rns = [None, 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii']
	return rns.index(rn)

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
		# print scale.__getitem__(i)
		if scale.__getitem__(i).letter.__eq__(theory.Note(note).letter):
			return i + 1
	raise ValueError("note ", note, " not in scale ", key)

def build_chord(num, key):
	# print "\n\nBUILDING CHORD: ", num, " chord in ", key
	scale = theory.Scale(key[0], key[1])
	letter = scale[num-1]

	if key[1] == 'major':
		ending = major_chords[num-1]

	if key[1] == 'harmonic_minor':
		ending = minor_chords[num-1]

	# print "\nChord is ", letter, ending, '\n\n'
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

	# print "chord options are ", sorted(options)
	return sorted(options)

def get_first_chord(first_note, key):
	options = get_chord_options(first_note, key)
	if key[0] in options:
		return build_chord(key[0], key)

	return build_chord(options[0], key)

def get_next_chord(next_note, prev_chord, key):

	# print '\n\nGETTING CHORD:\n'
	# print 'next_note: ', next_note
	# print 'prev_chord: ', prev_chord

	prev_chord_num = get_scale_idx(prev_chord[0], key)

	rand = random.seed()
	r = random.randint(1, 100) / float(100)

	if key[1] == 'major':
		probs = matrix[num_to_rn(prev_chord_num)]
		#print "probs are ", probs
	if key[1] == 'harmonic_minor':
		probs = matrix[num_to_rn(prev_chord_num)]
	# print "\nFull Probabilities: ", probs

	options = get_chord_options(next_note, key)
	options = [num_to_rn(option) for option in options]
	# print "\nOptions: ", options

	options_probs = []
	# for prob in probs:
	# 	if prob in options:
	# 		options_probs.append(probs[prob])

	for prob in options:
		options_probs.append(probs[prob])

	s = sum(options_probs)
	normalized = [prob/s for prob in options_probs]

	# print "\nNormalized Probabilities: ", normalized

	total = 0
	index = -1
	for i in range(0, len(normalized)):
		if r <= total + normalized[i]:
			index = i
			break
		total += normalized[i]

	return build_chord(rn_to_num(options[index]), key)

def get_all_chords(notes, key):
	first_note = notes[0]
	first_chord = get_first_chord(first_note, key)

	all_chords = [first_chord]

	prev_chord = first_chord
	print "notes are ", notes
	for note in notes[1:]:
		next_chord = get_next_chord(note, prev_chord, key)
		all_chords.append(next_chord)
		prev_chord = next_chord

	return all_chords

def write_chords_single(all_chords, path):
	tree = ET.parse(path)
	root = tree.getroot()
	P1 = root.find('part')
	prev_chord = None

	chord_counter = 0
	measure_counter = 0 #to find measure index to feed to add_chord
	for measure in P1.findall('measure'):
		note = measure.find('note')
		note_index = measure.getchildren().index(note)
		if len(note.findall('pitch')) != 0:
			curr_chord = all_chords[chord_counter]
			if curr_chord == prev_chord:
				chord_counter += 1
				measure_counter += 1
				print 'REPEATED CHORD DETECTED: skipping this write'
				continue

			if 'M' in curr_chord:
				mxml.add_chord(curr_chord[0:-1], 'major', measure_counter, note_index, tree)

			elif curr_chord.endswith('dim'):
				mxml.add_chord(curr_chord[0:-3], 'diminished', measure_counter, note_index, tree)

			elif curr_chord.endswith('m'):
				mxml.add_chord(curr_chord[0:-1], 'minor', measure_counter, note_index, tree)
			
			prev_chord = curr_chord
			chord_counter += 1
		measure_counter += 1

def write_chords(all_chords, path):
	tree = ET.parse(path)
	root = tree.getroot()
	P1 = root.find('part')
	prev_chord = None

	chord_counter = 0
	measure_counter = 0 #to find measure index to feed to add_chord
	for measure in P1.findall('measure'):
		for note in measure.findall('note'):
			note_index = measure.getchildren().index(note)
			if len(note.findall('pitch')) != 0:
				curr_chord = all_chords[chord_counter]
				if curr_chord == prev_chord:
					chord_counter += 1
					continue

				if 'M' in curr_chord:
					mxml.add_chord(curr_chord[0:-1], 'major', measure_counter, note_index, tree)

				elif curr_chord.endswith('dim'):
					mxml.add_chord(curr_chord[0:-3], 'diminished', measure_counter, note_index, tree)

				elif curr_chord.endswith('m'):
					mxml.add_chord(curr_chord[0:-1], 'minor', measure_counter, note_index, tree)
				
				prev_chord = curr_chord
				chord_counter += 1
		measure_counter += 1

def main():

	path = sys.argv[1]
	key_name = sys.argv[2]
	key_tonality = sys.argv[3]
	genre = sys.argv[4]
	rhythm = sys.argv[5]

	global matrix

	#build matrix based on tonality
	if key_tonality == 'major':
		matrix = dynamicMatrix.build_major_matrix(genre)
	elif key_tonality == 'harmonic_minor':
		matrix = dynamicMatrix.build_minor_matrix(genre)
	#write_chords(get_all_chords(mxml.get_notes(path), (key_name, key_tonality)), path)

	#build accompani based on rhythm input
	if rhythm == 'measure':
		write_chords_single(get_all_chords(mxml.get_notes_single(path, (key_name, key_tonality)), (key_name, key_tonality)), path)
	else:
		write_chords(get_all_chords(mxml.get_notes(path, (key_name, key_tonality)), (key_name, key_tonality)), path)
	mxml.format_document('accompani.xml')

main()
# matrix = dynamicMatrix.build_matrix('Rock')
# print get_all_chords(['F', 'D', 'Bb', 'D', 'F', 'Bb'], ('Bb', 'major'))

# print get_all_chords(['C', 'D', 'E', 'D', 'C'], ('C', 'major'))
