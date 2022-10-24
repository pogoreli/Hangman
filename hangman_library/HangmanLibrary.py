import random

'''This class is designed as backend to GUI and TUI versions of Hangman game'''
class HangmanLibrary:
    words = []
    lettersAlreadyUsed = []
    mistakesCount = 0
    score = 0
    word = ""
    arrayOfCorrectLetters = []

    '''The library imports the words from the file on startup'''
    def __init__(self):
        self.importWords()

    '''A function for word import. Removes short lines (less than 2 symbols) and removes the new line character'''
    def importWords(self):
        with open('words.txt') as file:
            for line in file:
                if len(line) >= 2:
                    self.words.append(line.rstrip().lower())

    '''Function called before each game. Resets score, mistakes count, and letters already used. Picks a new word for the game'''
    def startNewGame(self):
        self.mistakesCount = 0
        self.score = 0
        self.lettersAlreadyUsed = []
        self.word = self.pickRandomWord()
        self.arrayOfCorrectLetters.clear()
        for i in range(len(self.arrayOfCorrectLetters)-1):
            self.arrayOfCorrectLetters[i] = "_"



    '''Picks a word from the list'''
    def pickRandomWord(self):
        return random.choice(self.words)

    '''Receives a new letter from a user and checks wheter it was already used and whether it exists in the word'''
    def submitNewLetter(self, letter):
        if not self.checkIfLetterAlreadyUsed(letter):
            if self.checkIfLetterExists():
             self.score += 1
            else:
                self.mistakesCount += 1
        else:
            print("This letter has already been used")  #Need to add something to inform user or throw an error

    '''Checks if letter exists in the word. Returns True if exists in the word'''
    def checkIfLetterExists(self, letter) -> bool:
        for symbol in self.word:
            if symbol == letter:
                return True
        return False

    '''Checks whether letter was used in this round. Returns True if already used'''
    def checkIfLetterAlreadyUsed(self, letter) -> bool:
        for symbol in self.lettersAlreadyUsed:
            if symbol == letter:
                return True
        return False

    def getLetterPositionsInWord(self, letter):
        letterLower = str(letter).lower()
        for i in range(0,len(self.word)):
            if(letterLower == self.word[i]):
                self.arrayOfCorrectLetters[i] = letterLower
        return self.arrayOfCorrectLetters