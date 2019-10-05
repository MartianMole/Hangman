import random


def writeCurWord(word):
    print(*word)


def putLetter(letter, word):
    global xWord
    for i in range(len(word)):
        if xWord[i] == letter:
            word[i] = letter
    return word


liveCount = 5
dictionary = open('dictionary').read().splitlines()
xWord = random.choice(dictionary)
print(xWord)
curWord = ['_'] * len(xWord)
usedLetters = set()


def mainLoop():
    global liveCount
    writeCurWord(curWord)
    if '_' not in curWord:
        print('You win')
        exit()
    else:
        guessLetter = input()
        if guessLetter in usedLetters:
            print('You\'ve already picked this letter')
        else:
            if guessLetter in xWord:
                putLetter(guessLetter, curWord)
            else:
                liveCount -= 1
                if liveCount >= 0:
                    print(liveCount, 'lives left')
                else:
                    print(*xWord)
                    print('You loose(')
                    exit(0)
            usedLetters.add(guessLetter)
    mainLoop()


mainLoop()
