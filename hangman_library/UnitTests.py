import unittest
from HangmanLibrary import HangmanLibrary
# Method	                 Equivalent to
# .assertEqual(a, b)	     a == b
# .assertTrue(x)	         bool(x) is True
# .assertFalse(x)	         bool(x) is False
# .assertIs(a, b)	         a is b
# .assertIsNone(x)	         x is None
# .assertIn(a, b)	         a in b
# .assertIsInstance(a, b)	 isinstance(a, b)

class TestHangmanLibrary(unittest.TestCase):
    '''Unit test for the letter comparation function repetitive symbol'''
    def testLetterComparation1(self):
        testedObject = HangmanLibrary()
        testedObject.startNewGame()
        testedObject.arrayOfCorrectLetters = ["_","_","_","_","_"]
        testedObject.word = "apple"
        data = testedObject.getLetterPositionsInWord("p")
        self.assertEqual(data, ["_","p","p","_","_"])

    '''Test of letter comparation last symbol'''
    def testLetterComparation2(self):
        testedObject = HangmanLibrary()
        testedObject.startNewGame()
        testedObject.arrayOfCorrectLetters = ["_","_","_","_","_"]
        testedObject.word = "apple"
        data = testedObject.getLetterPositionsInWord("p")
        data = testedObject.getLetterPositionsInWord("e")
        self.assertEqual(data, ["_","p","p","_","e"])

    '''Test of letter comparation first symbol'''
    def testLetterComparation3(self):
        testedObject = HangmanLibrary()
        testedObject.startNewGame()
        testedObject.arrayOfCorrectLetters = ["_","_","_","_","_"]
        testedObject.word = "apple"
        data = testedObject.getLetterPositionsInWord("p")
        data = testedObject.getLetterPositionsInWord("e")
        data = testedObject.getLetterPositionsInWord("a")
        self.assertEqual(data, ["a","p","p","_","e"])

    '''Test of letter comparation different case'''
    def testLetterComparation4(self):
        testedObject = HangmanLibrary()
        testedObject.startNewGame()
        testedObject.arrayOfCorrectLetters = ["_","_","_","_","_"]
        testedObject.word = "apple"
        data = testedObject.getLetterPositionsInWord("P")
        self.assertEqual(data, ["_","p","p","_","_"])


if __name__ == '__main__':
    unittest.main()