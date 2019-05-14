'''
C to Roman Numerals
outputs an array of roman numerals of same length as input array
'''
def c_to_rn(c_array):
	roman_numerals = []

	for chord in c_array:
		if chord.startswith("C"):
			roman_numerals.append("i" + chord[1:])
		elif chord.startswith("Dm"):
			roman_numerals.append("ii" + chord[2:])
		elif chord.startswith("Em"):
			roman_numerals.append("iii" + chord[2:])
		elif chord.startswith("F"):
			roman_numerals.append("iv" + chord[1:])
		elif chord.startswith("G"):
			roman_numerals.append("v" + chord[1:])
		elif chord.startswith("Am"):
			roman_numerals.append("vi" + chord[2:])
		else: 	#starts with Bdim (diminished 7th chord)
			roman_numerals.append("vii" + chord)

	return roman_numerals

print "original is ", ['C', 'F', 'C', 'Dm', 'Am', 'G', 'Gsus4', 'G', 'C', 'F', 'C', 'Dm', 'Am', 'G', 'Gsus4', 'G', 'Am', 'Dm', 'C', 'F', 'G', 'C', 'F', 'C', 'Dm', 'F', 'C', 'C', 'F', 'C', 'F', 'C', 'F', 'C', 'F', 'C', 'Dm', 'Am', 'G', 'Gsus4', 'G', 'C', 'F', 'C', 'Dm', 'Am', 'G', 'Gsus4', 'G', 'Am', 'Dm', 'C', 'F', 'G', 'C', 'F', 'C', 'Dm', 'F', 'C', 'C', 'F', 'C', 'F', 'C', 'F', 'F', 'C', 'F', 'C', 'G', 'C', 'F', 'C', 'Dm', 'Am', 'G', 'Gsus4', 'G', 'C', 'F', 'C', 'Dm', 'Am', 'G', 'Gsus4', 'G', 'Am', 'Dm', 'C', 'F', 'G', 'C', 'F', 'C', 'Dm', 'F', 'C', 'C', 'F', 'C', 'F', 'C', 'F'] 
print "rn is       ", c_to_rn(['C', 'F', 'C', 'Dm', 'Am', 'G', 'Gsus4', 'G', 'C', 'F', 'C', 'Dm', 'Am', 'G', 'Gsus4', 'G', 'Am', 'Dm', 'C', 'F', 'G', 'C', 'F', 'C', 'Dm', 'F', 'C', 'C', 'F', 'C', 'F', 'C', 'F', 'C', 'F', 'C', 'Dm', 'Am', 'G', 'Gsus4', 'G', 'C', 'F', 'C', 'Dm', 'Am', 'G', 'Gsus4', 'G', 'Am', 'Dm', 'C', 'F', 'G', 'C', 'F', 'C', 'Dm', 'F', 'C', 'C', 'F', 'C', 'F', 'C', 'F', 'F', 'C', 'F', 'C', 'G', 'C', 'F', 'C', 'Dm', 'Am', 'G', 'Gsus4', 'G', 'C', 'F', 'C', 'Dm', 'Am', 'G', 'Gsus4', 'G', 'Am', 'Dm', 'C', 'F', 'G', 'C', 'F', 'C', 'Dm', 'F', 'C', 'C', 'F', 'C', 'F', 'C', 'F'] )

