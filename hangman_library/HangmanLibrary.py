import random

class HangmanLibrary:
    words = []
    lettersAlreadyUsed = []
    mistakesCount = 0
    score = 0
    word = ""

    def __init__(self):
        self.importWords()

    def importWords(self):
        with open('words.txt') as file:
            for line in file:
                if len(line) >= 2:
                    self.words.append(line.rstrip())

    def startNewGame(self):
        self.mistakesCount = 0
        self.score = 0
        self.lettersAlreadyUsed = []
        self.word = self.pickRandomWord()

    def pickRandomWord(self):
        return random.choice(self.words)

    def submitNewLetter(self, letter):
        if not self.checkIfLetterAlreadyUsed(letter):
            if self.checkIfLetterExists():
             self.score += 1
            else:
                self.mistakesCount += 1
        else:
            print("This letter has already been used")  #Need to add something to inform user or throw an error

    def checkIfLetterExists(self, letter) -> bool:
        for symbol in self.word:
            if symbol == letter:
                return True
        return False

    def checkIfLetterAlreadyUsed(self, letter) -> bool:
        for symbol in self.lettersAlreadyUsed:
            if symbol == letter:
                return True
        return False