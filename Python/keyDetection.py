import os,sys, re, operator

def sortKeyScores(keyScores): 
    return [score for score in reversed(keyScores)] 

def parseChordpro(path):
    title = path
    key = open(path).readline().split(' ')[1].split('}')[0]
    text = open(path).read()
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
        "E":["E","F#m","G#m","A","B","C#m","D#dim"],
        "F":["F","Gm","Am","Bb","C","Dm","Edim"],
        "F#":["F#","G#m","A#m","B","C#","D#m","E#dim"],
        "Gb":["Gb","Abm","Bbm","Cb","Db","Ebm","Fdim"],
        "G":["G","Am","Bm","C","D","Em","F#dim"],
        "Ab":["Ab","Bbm","Cm","Db","Eb","Fm","Gdim"],
        "A":["A","Bm","C#m","D","E","F#m","G#dim"],
        "Bb":["Bb","Cm","Dm","Eb","F","Gm","Adim"],
        "B":["B","C#m","D#m","E","F#","G#m","A#dim"],
    }
    minorKeys = {
        "Am":["Am","Bdim","C","Dm","E","F","G"],
        "A#m":["A#m","B#dim","C#","D#m","E#","F#","G#"],
        "Bbm":["Bbm","Cdim","Db","Ebm","F","Gb","Ab"],
        "Bm":["Bm","C#dim","D","Em","F#","G","A"],
        "Cm":["Cm","Ddim","Eb","Fm","G","Ab","Bb"],
        "C#m":["C#m","D#dim","E","F#m","G#","A","B"],
        "Dbm":["Dbm","Ebdim","E","Gbm","Ab","Bb","B"],
        "Dm":["Dm","Edim","F","Gm","A","Bb","C"],
        "D#m":["D#m","E#dim","F#","G#m","A#","B","C#"],
        "Ebm":["Ebm","Fdim","Gb","Abm","Bb","Cb","Db"],
        "Em":["Em","F#dim","G","Am","B","C","D"],
        "Fm":["Fm","Gdim","Ab","Bbm","C","Db","Eb"],
        "F#m":["F#m","G#dim","A","Bm","C#","D","E"],
        "Gm":["Gm","Adim","Bb","Cm","D","Eb","F"],
        "G#m":["G#m","A#dim","B","C#m","D#","E","F#"],
        "Abm":["Abm","Bbdim","B","Dbm","Eb","F","Gb"]
    }



    majorKeyScores = {"C":0,"C#":0,"Db":0,"D":0,"Eb":0,"E":0,"F":0,"F#":0,"Gb":0,"G":0,"Ab":0,"A":0,"Bb":0,"B":0}
    minorKeyScores = {"Cm":0,"C#m":0,"Dbm":0,"Dm":0,"D#m":0,"Ebm":0,"Em":0,"Fm":0,"F#m":0,"Gbm":0,"Gm":0,"G#m":0,"Abm":0,"Am":0,"A#m":0,"Bbm":0,"Bm":0}
    
    for chord in chords:
        for keySignature in majorKeys:
            keySig = majorKeys[keySignature]
            if 'm' in chord:
                if keySig[1] in chord:
                    # 2nd detection
                    majorKeyScores[keySignature] += 15

                if keySig[5] in chord:
                    # 6th detection
                    majorKeyScores[keySignature] += 15

                if keySig[2] in chord:
                    # 3rd detection
                    majorKeyScores[keySignature] += 10

                if keySig[6] in chord:
                    # 7th detection
                    majorKeyScores[keySignature] += 10

            if 'm' not in chord:
                if keySig[0] in chord:
                    # root detection
                    majorKeyScores[keySignature] += 25

                if keySig[4] in chord:
                    # 5th detection
                    majorKeyScores[keySignature] += 12
                if keySig[3] in chord:
                    # 4th detection
                    majorKeyScores[keySignature] += 15
        for keySignature in minorKeys:
            keySig = minorKeys[keySignature]
            if 'm' in chord:
                if keySig[3] in chord:
                    # 4th detection
                    minorKeyScores[keySignature] += 15
                if keySig[1] in chord:
                    # 2nd detection
                    minorKeyScores[keySignature] += 5
                if keySig[0] in chord:
                    # root detection
                    minorKeyScores[keySignature] += 30

            if 'm' not in chord:
                if keySig[4] in chord:
                    # 5th detection
                    minorKeyScores[keySignature] += 20
                if keySig[6] in chord:
                    # 7th detection
                    minorKeyScores[keySignature] += 5
                if keySig[5] in chord:
                    # 6th detection
                    minorKeyScores[keySignature] += 15
                if keySig[2] in chord:
                    # 3rd detection
                    minorKeyScores[keySignature] += 12
                

    majorKeyScoresList = sortKeyScores(sorted(majorKeyScores.items(), key=operator.itemgetter(1)))
    minorKeyScoresList = sortKeyScores(sorted(minorKeyScores.items(), key=operator.itemgetter(1)))
    detectedMajorKey = max(majorKeyScores.iteritems(), key=operator.itemgetter(1))[0]
    detectedMinorKey = max(minorKeyScores.iteritems(), key=operator.itemgetter(1))[0]
    return majorKeyScoresList, minorKeyScoresList, detectedMajorKey, detectedMinorKey

def printResults(title,key,detectedMajorKey,majorKeyScoresList,detectedMinorKey,minorKeyScoresList,chordsInSong):

    max_major = majorKeyScoresList[0]
    max_minor = minorKeyScoresList[0]

    if max_major[1] >= max_minor[1]:
        highest = max_major[0]
    else:
        highest = max_minor[0]

    #if detectedKey != actualKey:
    if 'm' in key and highest != key:
        print title + ' in ' + key
        print '\n'
        print 'CHORDS:'
        print chordsInSong
        print '\n'
        print 'DETECTED MAJOR KEY: ' + detectedMajorKey + '\n'
        print 'MAJOR KEY SCORES:'
        print majorKeyScoresList
        print '\n'
        print 'DETECTED MINOR KEY: ' + detectedMinorKey + '\n'
        print 'MINOR KEY SCORES:'
        print minorKeyScoresList
        print'\n\n\n'

def printAccuracy(numSongs, numCorrect, numSongsMinor, numCorrectMinor):
    accuracy = numCorrect / float(numSongs) * 100
    accuracyMinor = numCorrectMinor / float(numSongsMinor) * 100
    print 'ACCURACY: ' + str(numCorrect) + '/' + str(numSongs) + ' -- ' + str(accuracy) + '%\n\n\n'
    print 'MINOR ACCURACY: ' + str(numCorrectMinor) + '/' + str(numSongsMinor) + ' -- ' + str(accuracyMinor) + '%\n\n\n'

def relative_minor(key):
    relative = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]


def main():

    # initialize accuracy counters
    numSongs = 0
    numCorrect = 0
    numSongsMinor = 0
    numCorrectMinor = 0

    # main method
    for artist in os.listdir('./training_data'):
        if artist == '.DS_Store':
                continue
        for filename in os.listdir('./training_data/' + artist):
            if filename == '.DS_Store':
                continue
            fullpath = './training_data/' +  artist + '/' + filename

            # load song data
            title, key, chordsInSong = parseChordpro(fullpath)

            # #skip nonminor keys
            # if key[-1] == 'm':
            #     continue

            # increment accuracy counter
            numSongs += 1

            # calculate key scores
            majorKeyScoresList, minorKeyScoresList, detectedMajorKey, detectedMinorKey = calculateKeyScores(chordsInSong)

                # increment accuracy counter if correct
            '''if key == detectedMajorKey:
                printResults(title,key,detectedMajorKey,majorKeyScoresList,detectedMinorKey,minorKeyScoresList,chordsInSong)
                numCorrect += 1
            elif key == detectedMinorKey:
                printResults(title,key,detectedMajorKey,majorKeyScoresList,detectedMinorKey,minorKeyScoresList,chordsInSong)
                numCorrect += 1'''
            #else:

            if majorKeyScoresList[0][1] >= minorKeyScoresList[0][1]:
                winner = detectedMajorKey
            else:
                winner = detectedMinorKey

            if 'm' in key:
                numSongsMinor += 1

            if key == winner:
                numCorrect += 1
                if 'm' in key:
                    numCorrectMinor += 1 
            else:
                printResults(title,key,detectedMajorKey,majorKeyScoresList,detectedMinorKey,minorKeyScoresList,chordsInSong)
                

    printAccuracy(numSongs,numCorrect, numSongsMinor, numCorrectMinor)

main()
