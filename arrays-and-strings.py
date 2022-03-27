import unittest

def isUnique (str_to_analyze):
    characterSet = set(str_to_analyze)
    if len(str_to_analyze) == len (characterSet):
        return True
    else:
        return False





class TestsForChapter(unittest.TestCase):

    def test_isUnique(self):
        self.assertTrue(isUnique("question"))
        self.assertTrue(isUnique("dog"))
        self.assertTrue(isUnique("abcdefghijklmnopqrst123"))
        self.assertFalse(isUnique("bedroom"))
        self.assertFalse(isUnique("abcdefrghijklmnopqrst123"))


if __name__ == '__main__':
    unittest.main()


