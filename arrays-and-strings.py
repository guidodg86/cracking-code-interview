import unittest
import re

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

def urliFy (data_string):
    return re.sub(r"[ ]+", "%20", data_string)


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

    def test_urliFy(self):
        self.assertEqual(urliFy("nospaces"), "nospaces")
        self.assertEqual(urliFy("one space between"), "one%20space%20between")
        self.assertEqual(urliFy("more    spaces    between"), "more%20spaces%20between")
        self.assertEqual(urliFy("mix  of   spaces and  space at  end  "), "mix%20of%20spaces%20and%20space%20at%20end%20")



if __name__ == '__main__':
    unittest.main()


