import os,sys, re, operator

def sortKeyScores(keyScores): 
    return [score for score in reversed(keyScores)] 

def parseChordpro(filepath):
    title = filepath.split('.')[0]
    # print title
    #key = open('./chordpro/d/Bob.Dylan/' + filename).readline().split(' ')[1].split('}')[0]
    key = '?'
    text = open(filepath).read()
    chords = text.split('[')[1:]
    for i in range(len(chords)):
        chords[i] = chords[i].split(']')[0]
    return title, key, chords

def calculateKeyScores(chords):
    # initialize key signatures
    majorKeys = {
        "C":["C","Dm","Em","F","G","Am","Bdim"],
        "C#":["C#","D#m","E#m","F#","G#","A#m","B#dim"],
        "Db":["Db","Ebm","Fm","Gb","Ab","Bbm","Cdim"],
        "D":["D","Em","F#m","G","A","Bm","C#dim"],
        "Eb":["Eb","Fm","Gm","Ab","Bb","Cm","Ddim"],
        "E":["E","F#m","G#m","A","B","C#m","`D#dim"],
        "F":["F","Gm","Am","Bb","C","Dm","Edim"],
        "F#":["F#","G#m","A#m","B","C#","D#m","E#dim"],
        "Gb":["Gb","Abm","Bbm","Cb","Db","Ebm","Fdim"],
        "G":["G","Am","Bm","C","D","Em","F#dim"],
        "Ab":["Ab","Bbm","Cm","Db","Eb","Fm","Gdim"],
        "A":["A","Bm","C#m","D","E","F#m","G#dim"],
        "Bb":["Bb","Cm","Dm","Eb","F","Gm","Adim"],
        "B":["B","C#m","D#m","E","F#","G#m","A#dim"],
    }
    keyScores = {"C":0,"C#":0,"Db":0,"D":0,"Eb":0,"E":0,"F":0,"F#":0,"Gb":0,"G":0,"Ab":0,"A":0,"Bb":0,"B":0}
    for chord in chords:
        for keySignature in majorKeys:
            for chordInKeySignature in majorKeys[keySignature]:
                if chordInKeySignature in chord:
                    if 'm' in chordInKeySignature and 'm' in chord:
                        keyScores[keySignature] += 1
                    if 'm' not in chordInKeySignature and 'm' not in chord:
                        keyScores[keySignature] += 1
    keyScoresList = sortKeyScores(sorted(keyScores.items(), key=operator.itemgetter(1)))  
    detectedKey = max(keyScores.iteritems(), key=operator.itemgetter(1))[0]
    return keyScoresList, detectedKey



def detectKey(filename):
    
    title, key, chordsInSong = parseChordpro(filename)
    keyScores, detectedKey = calculateKeyScores(chordsInSong)

    return detectedKey

