import random


def writeCurWord(word):
    print(*word)


def putLetter(letter, word):
    global xWord
    for i in range(len(word)):
        if xWord[i] == letter:
            word[i] = letter
    return word


lifeCount = 5
xWord = [i for i in 'apple']
print(xWord)
curWord = ['_'] * 5
usedLetters = []


def mainLoop():
    global lifeCount
    writeCurWord(curWord)
    if '_' not in curWord:
        print('You win')
        exit()
    else:
        guessLetter = input()
        if guessLetter in xWord:
            putLetter(guessLetter, curWord)
        else:
            lifeCount -= 1
            if lifeCount >= 0:
                print(lifeCount, 'lifes remain')
            else:
                print(*xWord)
                print('You loose(')
                exit(0)
    mainLoop()


mainLoop()