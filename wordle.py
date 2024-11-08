# Write your code here :-)
from wordleDictionary import list1

numCorrectLetters = int(input("How many green letters are there? "))
correctLSpot = [ ]
wordCorrectFirst = [ ]
wordCorrectSecond = [ ]
wordCorrectThird = [ ]
wordCorrectFourth = [ ]
wordCorrectFifth = [ ]
correctWord1 = [ ]



def correctL3tt3rs():

    if(numCorrectLetters > 5):
        print("error")

    else:
        for i in range(numCorrectLetters):
            correctLetters = input("What is the green letter, if more than one, input one at a time ")
            correctLetterSpot = int(input("Which spot is the letter located at "))
            correctLSpot.append(correctLetterSpot)
            for i in range(len(list1)):
                word = list1[i]
                if(correctLetterSpot == 1):
                    if(word[0:1] == correctLetters):
                        wordCorrectFirst.append(word)

                elif(correctLetterSpot >=2):
                    if(correctLetterSpot > 5):
                        print("error incorrect letter placement")
                        break
                    elif(correctLetterSpot == 2):
                        if(word[1:2] == correctLetters):
                            wordCorrectSecond.append(word)
                    elif(correctLetterSpot == 3):
                        if(word[2:3] == correctLetters):
                            wordCorrectThird.append(word)
                    elif(correctLetterSpot == 4):
                        if(word[3:4] == correctLetters):
                            wordCorrectFourth.append(word)
                    elif(correctLetterSpot == 5):
                        if(word[4] == correctLetters):
                            wordCorrectFifth.append(word)
            #print("words w/ first letter correct: " + str(wordCorrectFirst))
            #print("words w/ second letter correct: " + str(wordCorrectSecond))
            #print("words w/ third letter correct: " + str(wordCorrectThird))
            #print("words w/ fourth letter correct: " + str(wordCorrectFourth))
            #print("words w/ fifth letter correct: " + str(wordCorrectFifth))

def compareCLwords(numCorrectLetters, correctLetterSpot, wordCorrectFirst, wordCorrectSecond, wordCorrectThird, wordCorrectFourth, wordCorrectFifth):
    if(numCorrectLetters > 1):
        for r in range(len(correctLSpot)):
            if(correctLSpot[r] == 1):
                for i in range(len(wordCorrectFirst)):
                    word3 = wordCorrectFirst[i]
                    for h in range(len(wordCorrectSecond)):
                        word4 = wordCorrectSecond[h]
                        if(word3 == word4):
                            correctWord1.append(word3)
                    for t in range(len(wordCorrectThird)):
                        word5 = wordCorrectThird[t]
                        if(word3 == word5):
                            correctWord1.append(word3)
                    for j in range(len(wordCorrectFourth)):
                        word6 = wordCorrectFourth[j]
                        if(word3 == word6):
                            correctWord1.append(word3)
                    for k in range(len(wordCorrectFifth)):
                        word7 = wordCorrectFifth[k]
                        if(word3 == word7):
                            correctWord1.append(word3)
            elif(correctLSpot[r] == 2):
                for i in range(len(wordCorrectSecond)):
                    word3 = wordCorrectSecond[i]
                    for h in range(len(wordCorrectFirst)):
                        word4 = wordCorrectFirst[h]
                        if(word3 == word4):
                            correctWord1.append(word3)
                    for t in range(len(wordCorrectThird)):
                        word5 = wordCorrectThird[t]
                        if(word3 == word5):
                            correctWord1.append(word3)
                    for j in range(len(wordCorrectFourth)):
                        word6 = wordCorrectFourth[j]
                        if(word3 == word6):
                            correctWord1.append(word3)
                    for k in range(len(wordCorrectFifth)):
                        word7 = wordCorrectFifth[k]
                        if(word3 == word7):
                            correctWord1.append(word3)
            elif(correctLSpot[r] == 3):
                for i in range(len(wordCorrectThird)):
                    word3 = wordCorrectThird[i]
                    for h in range(len(wordCorrectFirst)):
                        word4 = wordCorrectFirst[h]
                        if(word3 == word4):
                            correctWord1.append(word3)
                    for t in range(len(wordCorrectSecond)):
                        word5 = wordCorrectSecond[t]
                        if(word3 == word5):
                            correctWord1.append(word3)
                    for j in range(len(wordCorrectFourth)):
                        word6 = wordCorrectFourth[j]
                        if(word3 == word6):
                            correctWord1.append(word3)
                    for k in range(len(wordCorrectFifth)):
                        word7 = wordCorrectFifth[k]
                        if(word3 == word7):
                            correctWord1.append(word3)
            elif(correctLSpot[r] == 4):
                for i in range(len(wordCorrectFourth)):
                    word3 = wordCorrectFourth[i]
                    for h in range(len(wordCorrectFirst)):
                        word4 = wordCorrectFirst[h]
                        if(word3 == word4):
                            correctWord1.append(word3)
                    for t in range(len(wordCorrectThird)):
                        word5 = wordCorrectThird[t]
                        if(word3 == word5):
                            correctWord1.append(word3)
                    for j in range(len(wordCorrectSecond)):
                        word6 = wordCorrectSecond[j]
                        if(word3 == word6):
                            correctWord1.append(word3)
                    for k in range(len(wordCorrectFifth)):
                        word7 = wordCorrectFifth[k]
                        if(word3 == word7):
                            correctWord1.append(word3)
            elif(correctLSpot[r] == 5):
                for i in range(len(wordCorrectFifth)):
                    word3 = wordCorrectFifth[i]
                    for h in range(len(wordCorrectFirst)):
                        word4 = wordCorrectFirst[h]
                        if(word3 == word4):
                            correctWord1.append(word3)
                    for k in range(len(wordCorrectSecond)):
                        word7 = wordCorrectFifth[k]
                        if(word3 == word7):
                            correctWord1.append(word3)
                    for t in range(len(wordCorrectThird)):
                        word5 = wordCorrectThird[t]
                        if(word3 == word5):
                            correctWord1.append(word3)
                    for j in range(len(wordCorrectFourth)):
                        word6 = wordCorrectFourth[j]
                        if(word3 == word6):
                            correctWord1.append(word3)
        #print(correctWord1)
numMisplacedLetters = int(input("How many yellow letters are there "))
misplacedLetterSpot = [ ]
misplacedLSpot = [ ]
wordMisplaced = [ ]
mLetter = [ ]
def misplacedWord():
    if(numMisplacedLetters > 5):
        print("error")

    else:
        for i in range(numMisplacedLetters):
            mLetters = input("What is the yellow letter, if more than one, input one at a time ")
            mLetter.append(mLetters)

            misplacedLetterSpot = int(input("Which spot is the letter located at "))
            misplacedLSpot.append(misplacedLetterSpot)

            if(numMisplacedLetters == 1):
                word13 = mLetter[0:1]
                for w in range(len(list1)):
                    num3 = len(word13)
                    word12 = list1[w]
                    if(word12[0:1] == word13[num3-1]):
                        wordMisplaced.append(word12)
                    elif(word12[1:2] == word13[num3-1]):
                        wordMisplaced.append(word12)
                    elif(word12[2:3] == word13[num3-1]):
                        wordMisplaced.append(word12)
                    elif(word12[3:4] == word13[num3-1]):
                        wordMisplaced.append(word12)
                    elif(word12[4] == word13[num3-1]):
                        wordMisplaced.append(word12)


            elif(numMisplacedLetters == 2):
                word14 = mLetter
                num4 = len(word14)
                for n in range(len(list1)):
                    if(num4 == 2):
                        word11 = list1[n]
                        if(word11[0:1] == word14[0]):
                            if(word11[1:2] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[2:3] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[3:4] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[4] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[0:1] == word14[num4-1]):
                                wordMisplaced.append(word11)
                        elif(word11[1:2] == word14[0]):
                            if(word11[0:1] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[1:2] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[2:3] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[3:4] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[4] == word14[num4-1]):
                                wordMisplaced.append(word11)
                        elif(word11[2:3] == word14[0]):
                            if(word11[0:1] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[1:2] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[2:3] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[3:4] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[4] == word14[num4-1]):
                                wordMisplaced.append(word11)
                        elif(word11[3:4] == word14[0]):
                            if(word11[0:1] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[1:2] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[2:3] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[3:4] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[4] == word14[num4-1]):
                                wordMisplaced.append(word11)
                        elif(word11[4] == word14[0]):
                            if(word11[0:1] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[1:2] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[2:3] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[3:4] == word14[num4-1]):
                                wordMisplaced.append(word11)
                            elif(word11[4] == word14[num4-1]):
                                wordMisplaced.append(word11)

            elif(numMisplacedLetters == 3):
                word15 = mLetter
                num5 = len(word15)
                for d in range(len(list1)):
                    if(num5 == 3):
                        word16 = list1[d]
                        if(word16[0:1] == word15[0]):
                            if(word16[0:1] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[1:2] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[2:3] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[3:4] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[4:5] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                        elif(word16[1:2] == word15[0]):
                            if(word16[0:1] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[1:2] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[2:3] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[3:4] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[4:5] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                        elif(word16[2:3] == word15[0]):
                            if(word16[0:1] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[1:2] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[2:3] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[3:4] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[4:5] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                        elif(word16[3:4] == word15[0]):
                            if(word16[0:1] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[1:2] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[2:3] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[3:4] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[4:5] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                        elif(word16[4] == word15[0]):
                            if(word16[0:1] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[1:2] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[2:3] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[3:4] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                            elif(word16[4:5] == word15[num5-2]):
                                if(word16[0:1] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[1:2] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[2:3] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[3:4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
                                elif(word16[4] == word15[num5-1]):
                                    wordMisplaced.append(word16)
            elif(numMisplacedLetters == 4):
                word17 = mLetter
                num6 = len(word17)
                for y in range(len(list1)):
                    if(num6 == 4):
                        word18 = list1[y]
                        if(word18[0:1] == word17[0]):
                            if(word18[0:1] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[1:2] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[2:3] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[3:4] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[4] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                        elif(word18[1:2] == word17[0]):
                            if(word18[0:1] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[1:2] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[2:3] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[3:4] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[4] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                        elif(word18[2:3] == word17[0]):
                            if(word18[0:1] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[1:2] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[2:3] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[3:4] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[4] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                        elif(word18[3:4] == word17[0]):
                            if(word18[0:1] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[1:2] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[2:3] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[3:4] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[4] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                        elif(word18[4] == word17[0]):
                            if(word18[0:1] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[1:2] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[2:3] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[3:4] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                            elif(word18[4] == word17[num6-3]):
                                if(word18[0:1] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[1:2] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[2:3] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[3:4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                elif(word18[4] == word17[num6-2]):
                                    if(word18[0:1] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[1:2] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[2:3] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[3:4] == word17[num6-1]):
                                        wordMisplaced.append(word18)
                                    elif(word18[4] == word17[num6-1]):
                                        wordMisplaced.append(word18)

            elif(numMisplacedLetters == 5):
                word19 = mLetter
                num7 = len(word19)
                for y in range(len(list1)):
                    if(num7 == 5):
                        word20 = list1[y]
                        if(word20[0:1] == word19[0]):
                            if(word20[0:1] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[1:2] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[2:3] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[3:4] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[4] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                        elif(word20[1:2] ==word19[0]):
                            if(word20[0:1] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[1:2] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[2:3] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[3:4] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[4] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                        elif(word20[2:3] ==word19[0]):
                            if(word20[0:1] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[1:2] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[2:3] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[3:4] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[4] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                        elif(word20[3:4] ==word19[0]):
                            if(word20[0:1] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[1:2] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[2:3] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[3:4] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[4] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                        elif(word20[4] ==word19[0]):
                            if(word20[0:1] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[1:2] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[2:3] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[3:4] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                            elif(word20[4] == word19[num7-4]):
                                if(word20[0:1] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[1:2] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[2:3] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[3:4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                elif(word20[4] == word19[num7-3]):
                                    if(word20[0:1] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[1:2] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[2:3] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[3:4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                    elif(word20[4] == word19[num7-2]):
                                        if(word20[0:1] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[1:2] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[2:3] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[3:4] == word19[num7-1]):
                                            wordMisplaced.append(word20)
                                        elif(word20[4] == word19[num7-1]):
                                            wordMisplaced.append(word20)

Words = [ ]

def compareWords(wordMisplaced, correctWord1):
    for i in range(len(wordMisplaced)):
        word32 = wordMisplaced[i]
        for l in range(len(correctWord1)):
            word42 = correctWord1[l]
            if(word32 == word42):
                Words.append(word32)

    print(Words)



correctL3tt3rs()
compareCLwords(numCorrectLetters, correctLSpot, wordCorrectFirst, wordCorrectSecond, wordCorrectThird, wordCorrectFourth, wordCorrectFifth)
misplacedWord()
compareWords(wordMisplaced, correctWord1)
