import xml.etree.ElementTree as ET
import musthe as theory


def get_notes(path, key):
	tree = ET.parse(path)
	root = tree.getroot()
	scale = theory.Scale(key[0], key[1])


	P1 = root.find('part')

	all_notes = []

	for measure in P1:
		for note in measure.findall('note'):
			if note.find('accidental') is not None:
				raise ValueError('\n\nWARNING: sorry mate, no notes outside the key signature for now. check back soon...\n\n')
			elif note.find('pitch') is not None:
				for i in range(7):
					if scale[i].letter == note.find('pitch').find('step').text:
						all_notes.append(str(scale[i].letter) + str(scale[i].accidental))

	return all_notes

def format_accidental(text):
	if text == 'natural':
		return ''
	elif text == 'flat':
		return 'b'
	elif text == 'sharp':
		return '#'

# print get_notes('/Users/ryanmchenry/Desktop/national_anthem.musicxml', ('Bb','major'))

def build_chord(name, ending):

	harmony = ET.Element('harmony')
	r = ET.SubElement(harmony, 'root')
	root_step = ET.SubElement(r, 'root-step')
	root_step.text = name
	kind = ET.SubElement(harmony, 'kind')
	kind.set('text', ending[0:3])
	kind.text = ending

	if name.endswith('b'):
		root_alter = ET.SubElement(r, 'root-alter')
		root_alter.text = '-1'
	elif name.endswith('#'):
		root_alter = ET.SubElement(r, 'root-alter')
		root_alter.text = '1'

	# the thing inside the XML element needs to be from the list of 33 MXML kind

	return harmony

def add_chord(chord_name, chord_ending, measure_index, note_index, tree):
	#tree = ET.parse(path)
	root = tree.getroot()
	P1 = root.find('part')
	measures = P1.findall('measure')

	measure = measures[measure_index]

	measure.insert(note_index, build_chord(chord_name, chord_ending))

	tree.write('accompani.xml')

def add_header(tree):
	root = tree.getroot()

def add_many_chords(chord_name, chord_ending, path):
	tree = ET.parse(path)
	root = tree.getroot()
	P1 = root.find('part')

	measure_counter = 0 #to find measure index to feed to add_chord
	for measure in P1.findall('measure'):
		for note in measure.findall('note'):
			note_index = measure.getchildren().index(note)
			if len(note.findall('pitch')) != 0:
				add_chord(chord_name, chord_ending, measure_counter, note_index, tree)
		measure_counter += 1
		
#print get_notes('Test.xml')
#add_many_chords('C', 'maj', 'Test.xml')
