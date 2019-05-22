import os,sys
import transpose
import rna
#import detectKey
import keyDetection
import warnings

#endings = ['7', '9', 'sus4', '7+', '6', '7add9','7sus', 'sus', '+7', '7(V)','7/4']

probabilities = {}

def transposeChords(filepath):
	keyVals_flat = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
	keyVals_sharp = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
	key = keyDetection.detectKey(filepath)

	chords = open(filepath).read().split('[')[1:]

	for i in range(len(chords)):
		chords[i] = chords[i].split(']')[0].split('/')[0]
		chords[i] = chords[i].capitalize()

	key = keyDetection.detectKey(filepath)

	if 'm' in key:
		key = key[0:-1]

	if key in keyVals_flat:
		keyVal = keyVals_flat.index(key)
	else:
		keyVal = keyVals_sharp.index(key)

	for i in range(len(chords)):
		curRoot, accidental = getChordVal(chords[i])
		if curRoot == -1:
		    # raise Warning('Non-transposable chord detected in ' + filepath)
		    warnings.warn('Non-transposable chord detected in ' + filepath + ': ' + chords[i])
		    continue
		newRoot = curRoot - keyVal
		if newRoot < 0:
		    newRoot += 12
		if accidental:
			if key in keyVals_flat:
				chords[i] = keyVals_flat[newRoot] + chords[i][2:]
				chords[i] = keyVals_flat[newRoot] + chords[i][1:]
			else:
				chords[i] = keyVals_sharp[newRoot] + chords[i][2:]
				chords[i] = keyVals_sharp[newRoot] + chords[i][1:]

	#print 'Transposed Chords: '
	#print chords, '\n\n\n\n\n'
	return chords

def getChordVal(chord):
	keyVals = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
	if chord[0] not in keyVals:
		return -1, None
	if len(chord) > 1:
		if chord[1] == '#':
			return keyVals.index(chord[0]) + 1, '#'
		if chord[1] == 'b':
			return keyVals.index(chord[0]) - 1, 'b'
	return keyVals.index(chord[0]), None

def fill_matrix(chords):
	idx = 0
	for chord in chords[:-1]: #looking at 2 chords at the same time

		num = chord_number(chord)
		num_next = chord_number(chords[idx+1])

		if in_dict(probabilities, num):
			if in_dict(probabilities[num], num_next):
				probabilities[num][num_next] += 1
			else:
				probabilities[num][num_next] = 1
		else:
			probabilities[num] = {}
			probabilities[num][num_next] = 1

		idx += 1
	return probabilities

#figures out which chord it is in case it has weird stuff after it
def chord_number(chord):
	if chord.startswith("i"):
		if len(chord) > 1 and chord[1] != "i" and chord[1] != "v":
			return "i"
		elif len(chord) == 1:
			return "i"

	if chord.startswith("ii"):
		if len(chord) > 2 and chord[2] != "i":
			return "ii"
		elif len(chord) == 2:
			return "ii"

	if chord.startswith("iii"):
		return "iii"

	if chord.startswith("iv"):
		return "iv"

	if chord.startswith("v"):
		if len(chord) > 1 and chord[1] != "i":
			return "v"
		elif len(chord) == 1:
			return "v"

	if chord.startswith("vi"):
		if len(chord) > 2 and chord[2] != "i":
			return "vi"
		elif len(chord) == 2:
			return "vi"

	if chord.startswith("vii"):
		return "vii"

#says whether a key is in the specified dictionary already
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
		print total
		for key2 in list(dictionary[key1].keys()): #divide everything by total
			dictionary[key1][key2] /= float(total)
	return dictionary

"""def main():
	for filename in os.listdir('./chordpro/d/Bob.Dylan/'):
	    title = filename.split('.')[0]

	    '''key = open('./chordpro/b/Beatles/' + filename).readline().split(' ')[1].split('}')[0]
	    if key.endswith("m"): #minor key; skip it for the major matrix!
	    	continue'''
	    
	    fill_matrix(rna.c_to_rn(transposeChords(filename)))

	    '''transposed = transpose.transposeChords(filename)
	    rn = rna.c_to_rn(transposed)
	    matrix = fill_matrix(rn)
	    normalized = normalize(matrix)'''
	return normalize(probabilities)"""



#print main()
