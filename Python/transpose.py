import os,sys, re

keyVals = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']

def transposeChords(filename):
    title = filename.split('.')[0]
    key = open('./chordpro/c/Christmas.songs/' + filename).readline().split(' ')[1].split('}')[0]
    keyVal = keyVals.index(key[0])

    #print title, ' in ', key, '\n'

    chords = open('./chordpro/c/Christmas.songs/' + filename).read().split('[')[1:]

    for i in range(len(chords)):
        chords[i] = chords[i].split(']')[0].split('/')[0]

    #print 'Original Chords: '
    #print chords, '\n'
    for i in range(len(chords)):
        curRoot, accidental = getChordVal(chords[i])
        if curRoot == -1:
            raise Warning('Non-transposable chord detected in ' + title)
            continue
        newRoot = curRoot - keyVal
        if newRoot < 0:
            newRoot += 12
        if accidental:
            chords[i] = keyVals[newRoot] + chords[i][2:]  
        chords[i] = keyVals[newRoot] + chords[i][1:]

    #print 'Transposed Chords: '
    #print chords, '\n\n\n\n\n'
    return chords

def getChordVal(chord):
    if chord[0] not in keyVals:
        return -1, None
    if len(chord) > 1:
        if chord[1] == '#':
            return keyVals.index(chord[0]) + 1, '#'
        if chord[1] == 'b':
            return keyVals.index(chord[0]) - 1, 'b'
    return keyVals.index(chord[0]), None


#transposeChords()