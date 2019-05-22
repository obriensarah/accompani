import os,sys
import transpose
import rna
import probMatrix
#import detectKey
import keyDetection
import operator

probabilities = {}


def build_matrix(genre):
	for dirname in os.listdir(os.path.join('../training_data/genres', genre)):
		if dirname != '.DS_Store':
			for filename in os.listdir(os.path.join('../training_data/genres', genre, dirname)):
				probabilities = probMatrix.fill_matrix(rna.c_to_rn(probMatrix.transposeChords(os.path.join('../training_data/genres', genre, dirname, filename))))
	# print probMatrix.normalize(probabilities)
	normalbois = probMatrix.normalize(probabilities)
	return normalbois

	# for bigboi in normalbois:
	# 	print(bigboi)
	# 	sorted_smallbois = sorted(normalbois[bigboi].items(), key=operator.itemgetter(1), reverse=True)
	# 	for smallboi in sorted_smallbois:
	# 		print smallboi
	# 	print '\n'



def main():
	# sys.stdout = None
	print build_matrix('Folk')

#main()