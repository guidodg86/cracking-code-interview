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

def searchPalindrome (data_string):
    chars_in_string = {}
    len_of_letters = 0
    for letter in data_string.lower():
        if letter == " ":
            continue
        len_of_letters = len_of_letters + 1
        chars_in_string[letter] = chars_in_string.get(letter, 0) + 1
    if len_of_letters % 2 == 0:
        for character in chars_in_string:
            if chars_in_string[character] % 2 != 0:
                return False
    else:
        odd_flag = False
        for character in chars_in_string:
            if odd_flag and chars_in_string[character] % 2 != 0:
                return False
            if chars_in_string[character] % 2 != 0:
                odd_flag = True
    return True



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

    def test_palindrome(self):
        self.assertTrue(searchPalindrome("Mr Owl ate my metal worm"))
        self.assertTrue(searchPalindrome("Do geese see God"))
        self.assertTrue(searchPalindrome("Was it a car or a cat I saw"))
        self.assertTrue(searchPalindrome("Rats live on no evil star"))
        self.assertTrue(searchPalindrome("Step on no pets"))
        self.assertTrue(searchPalindrome("redivider"))
        self.assertTrue(searchPalindrome("deified"))
        self.assertTrue(searchPalindrome("civic"))
        self.assertTrue(searchPalindrome("radar"))
        self.assertTrue(searchPalindrome("level"))
        self.assertTrue(searchPalindrome("rotor"))
        self.assertTrue(searchPalindrome("kayak"))
        self.assertTrue(searchPalindrome("reviver"))
        self.assertTrue(searchPalindrome("racecar"))
        self.assertTrue(searchPalindrome("madam"))
        self.assertTrue(searchPalindrome("refer"))
        self.assertTrue(searchPalindrome("ate  Mr Owl  my metal worm"))
        self.assertTrue(searchPalindrome("Do  see Godgeese"))
        self.assertTrue(searchPalindrome("Was  a carit orI saw a cat "))
        self.assertTrue(searchPalindrome("Rats live on no evil star"))
        self.assertTrue(searchPalindrome("Steppets on no "))
        self.assertTrue(searchPalindrome("redderivi"))
        self.assertTrue(searchPalindrome("defiedi"))
        self.assertTrue(searchPalindrome("cvici"))
        self.assertTrue(searchPalindrome("arrad"))
        self.assertTrue(searchPalindrome("velle"))
        self.assertFalse(searchPalindrome("lio ate  Mr. Owl  my metal worm"))
        self.assertFalse(searchPalindrome("cat Do  see Godgeese"))
        self.assertFalse(searchPalindrome("peter Was  a carit orI saw a cat "))
        self.assertFalse(searchPalindrome("Rats live peter on no evil star"))
        self.assertFalse(searchPalindrome("Steppets camera on no "))
        self.assertFalse(searchPalindrome("redderivilkj"))
        self.assertFalse(searchPalindrome("defiporedi"))
        self.assertFalse(searchPalindrome("cviqwci"))
        self.assertFalse(searchPalindrome("arraqwd"))
        self.assertFalse(searchPalindrome("vellqwe"))


if __name__ == '__main__':
    unittest.main()


