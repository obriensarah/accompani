import os,sys
import transpose
import rna
import probMatrix
#import detectKey
import keyDetection
import operator

probabilities = {}

major_matrix = {}
minor_matrix = {}


# def build_matrix(genre):
# 	for dirname in os.listdir(os.path.join('../training_data/genres', genre)):
# 		if dirname != '.DS_Store':
# 			for filename in os.listdir(os.path.join('../training_data/genres', genre, dirname)):
# 				probabilities = probMatrix.fill_matrix(rna.c_to_rn(probMatrix.transposeChords(os.path.join('../training_data/genres', genre, dirname, filename))))
# 	# print probMatrix.normalize(probabilities)
# 	normalbois = probMatrix.normalize(probabilities)
# 	return normalbois

	# for bigboi in normalbois:
	# 	print(bigboi)
	# 	sorted_smallbois = sorted(normalbois[bigboi].items(), key=operator.itemgetter(1), reverse=True)
	# 	for smallboi in sorted_smallbois:
	# 		print smallboi
	# 	print '\n'

def build_major_matrix(genre):
	for dirname in os.listdir(os.path.join('../training_data/genres', genre)):
		if dirname != '.DS_Store':
			for filename in os.listdir(os.path.join('../training_data/genres', genre, dirname)):
				key = keyDetection.detectKey(os.path.join('../training_data/genres', genre, dirname, filename))
				if 'm' not in key:
					major_matrix = probMatrix.fill_matrix(rna.c_to_rn(probMatrix.transposeChords(os.path.join('../training_data/genres', genre, dirname, filename))))
	# print probMatrix.normalize(probabilities)
	normalbois = probMatrix.normalize(major_matrix)

	for bigboi in normalbois:
		print(bigboi)
		sorted_smallbois = sorted(normalbois[bigboi].items(), key=operator.itemgetter(1), reverse=True)
		for smallboi in sorted_smallbois:
			print smallboi
		print '\n'


	return normalbois

def build_minor_matrix(genre):
	for dirname in os.listdir(os.path.join('../training_data/genres', genre)):
		if dirname != '.DS_Store':
			for filename in os.listdir(os.path.join('../training_data/genres', genre, dirname)):
				key = keyDetection.detectKey(os.path.join('../training_data/genres', genre, dirname, filename))
				if 'm' in key:
					minor_matrix = probMatrix.fill_matrix(rna.c_to_rn(probMatrix.transposeChords(os.path.join('../training_data/genres', genre, dirname, filename))))
	# print probMatrix.normalize(probabilities)

	for key in minor_matrix:
		for rn in ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii']:
			if rn not in minor_matrix[key]:
				minor_matrix[key][rn] = 0

	normalbois = probMatrix.normalize(minor_matrix)

	for bigboi in normalbois:
		print(bigboi)
		sorted_smallbois = sorted(normalbois[bigboi].items(), key=operator.itemgetter(1), reverse=True)
		for smallboi in sorted_smallbois:
			print smallboi
		print '\n'


	return normalbois

def main():
	# sys.stdout = None
	# print build_major_matrix('Folk')
	build_minor_matrix('Pop')

main()