import unittest

def isUnique (str_to_analyze):
    characterSet = set(str_to_analyze)
    if len(str_to_analyze) == len (characterSet):
        return True
    else:
        return False


def isPermutation (string1, string2):
    chars_in_1 = {}
    for letter in string1:
        chars_in_1[letter] = chars_in_1.get(letter, 0) + 1
    chars_in_2 = {}
    for letter in string2:
        chars_in_2[letter] = chars_in_2.get(letter, 0) + 1
    return chars_in_1 == chars_in_2


class TestsForChapter(unittest.TestCase):

    def test_isUnique(self):
        self.assertTrue(isUnique("question"))
        self.assertTrue(isUnique("dog"))
        self.assertTrue(isUnique("abcdefghijklmnopqrst123"))
        self.assertFalse(isUnique("bedroom"))
        self.assertFalse(isUnique("abcdefrghijklmnopqrst123"))

    def test_isPermutation(self):
        self.assertTrue(isPermutation("qquestion", "stqionque"))
        self.assertTrue(isPermutation("dog" , "god"))
        self.assertTrue(isPermutation("velez" , "velez"))
        self.assertTrue(isPermutation("abcdefghijklmnopqrst123","lambcndoefgpqrsthij12k3"))
        self.assertFalse(isPermutation("bedroom", "houses1"))
        self.assertFalse(isPermutation("abcdefrghijklmnopqrst123", "abcdefrghijklmgnopqrst123"))
        self.assertFalse(isPermutation("notebook", "desktop"))
        self.assertFalse(isPermutation("notebook", "booknoti"))


if __name__ == '__main__':
    unittest.main()


