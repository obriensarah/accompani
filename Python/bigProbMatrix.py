import os,sys
import operator

probabilities = {}

def parseChordpro(filename):
	title = filename.split('.')[0]
	key = open('./chordpro/b/Beatles/' + filename).readline().split(' ')[1].split('}')[0]
	text = open('./chordpro/b/Beatles/' + filename).read()
	chords = text.split('[')[1:]
	for i in range(len(chords)):
		chords[i] = chords[i].split(']')[0]
	return title, key, chords

def fill_matrix(chords):
	idx = 0
	for chord in chords[:-1]: #looking at 2 chords at the same time

		next_chord = chords[idx+1]

		if in_dict(probabilities, chord):
			if in_dict(probabilities[chord], next_chord):
				probabilities[chord][next_chord] += 1
			else:
				probabilities[chord][next_chord] = 1
		else:
			probabilities[chord] = {}
			probabilities[chord][next_chord] = 1

		idx += 1
	return probabilities

def in_dict(dictionary, key):
	keys = list(dictionary.keys())
	if key in keys:
		return True
	else:
		return False

def normalize(dictionary):
	for key1 in list(dictionary.keys()):
		total = 0
		for key2 in list(dictionary[key1].keys()): #get total
			total += dictionary[key1][key2]
		# print total
		for key2 in list(dictionary[key1].keys()): #divide everything by total
			dictionary[key1][key2] /= float(total)
	return dictionary

def main():
	for filename in os.listdir('./chordpro/b/Beatles'):
		title, key, chords = parseChordpro(filename)
		fill_matrix(chords)
	normalbois = normalize(probabilities)
	for bigboi in normalbois:
		print(bigboi)
		sorted_smallbois = sorted(normalbois[bigboi].items(), key=operator.itemgetter(1), reverse=True)
		for smallboi in sorted_smallbois:
			print smallboi
		print '\n'
	# print normalize(probabilities)

main()