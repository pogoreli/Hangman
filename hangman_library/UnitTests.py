import unittest

# Method	                 Equivalent to
# .assertEqual(a, b)	     a == b
# .assertTrue(x)	         bool(x) is True
# .assertFalse(x)	         bool(x) is False
# .assertIs(a, b)	         a is b
# .assertIsNone(x)	         x is None
# .assertIn(a, b)	         a in b
# .assertIsInstance(a, b)	 isinstance(a, b)

class TestHangmanLibrary(unittest.TestCase):
    def testOne(self):
        self.assertTrue(False)

    def testTwo(self):
        self.assertTrue(True)

    def testThree(self):
        self.assertTrue(False)

    def testFour(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()