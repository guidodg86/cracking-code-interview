import unittest
import re
from xxlimited import new

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

def oneWay (data_string1, data_string2):
    chars_in_1 = {}
    chars_in_2 = {}
    delta_letter=0

    for letter in data_string1.lower():
        chars_in_1[letter] = chars_in_1.get(letter, 0) + 1        
    for letter in data_string2.lower():
        chars_in_2[letter] = chars_in_2.get(letter, 0) + 1 

    letters_set = set(data_string1 + data_string2)
    for letter in letters_set:
        delta_letter += abs(chars_in_1.get(letter, 0) - chars_in_2.get(letter, 0))

    if delta_letter == 2 and len(data_string1) == len(data_string2):
        return True
    if delta_letter > 1:
        return False
    else:
        return True

def rotateMatrix(input_matrix):
    reversed_matrix = reversed(input_matrix)
    new_list = list(zip(*reversed_matrix))
    final_matrix = [list(item) for item in new_list]
    return final_matrix


def zeroMatrix(input_matrix):
    zero_founded = False
    for row,line in enumerate(input_matrix):
        for column,element in enumerate(line):
            if element == 0:
                zero_founded = True
                zero_column  = column
                zero_row = row

    if not zero_founded:
        return input_matrix

    new_matrix=[]
    for row,line in enumerate(input_matrix):
        draft = []
        for column,element in enumerate(line):
            if column == zero_column or row == zero_row:
                draft.append(0)
            else:
                draft.append(element)
        new_matrix.append(draft)
    
    return new_matrix

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


    def test_oneWay(self):
        self.assertTrue(oneWay("pale", "ple"))
        self.assertTrue(oneWay("pales", "pale"))
        self.assertTrue(oneWay("pale", "bale"))
        self.assertFalse(oneWay("pale", "bake"))
        self.assertTrue(oneWay("woman", "poman"))
        self.assertTrue(oneWay("woman", "oman"))
        self.assertTrue(oneWay("woman", "woman1"))
        self.assertFalse(oneWay("woman", "man"))
        self.assertTrue(oneWay("Supercalifragilisticexpialidocious", "Supercalifrarilisticexpialidocious"))
        self.assertFalse(oneWay("Supercalifragilisticexpialidocious", "Supercalifragilisticexpialidocio"))
        self.assertTrue(oneWay("Supercalifragilisticexpialidocious", "Supercalifragilisticexpialidocioup"))
        self.assertFalse(oneWay("Supercalifragilisticexpialidocious", "Supercaadasxlifragilisticexpialidocio"))
        self.assertTrue(oneWay("Supercalifragilisticexpialidocious", "Supercalifragilisticexpialidocious1"))
        self.assertFalse(oneWay("Supercalifragilisticexpialidocious", "Supercalifaaaaaaragilisticexpialidocio"))

    def test_rotateMatrix(self):
        m1 = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],]
        m2 = [[7, 4, 1],
              [8, 5, 2],
              [9, 6, 3],]
        self.assertEqual(rotateMatrix(m1), m2)
        m3 = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
        m4 = [[13, 9, 5, 1],
              [14, 10, 6, 2],
              [15, 11, 7, 3],
              [16, 12, 8, 4]]
        self.assertEqual(rotateMatrix(m3), m4)


    def test_zeroMatrix(self):
        m1 = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
        m2 = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
        self.assertEqual(zeroMatrix(m1), m2)
        m1 = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 0, 12],
              [13, 14, 15, 16]]
        m2 = [[1, 2, 0, 4],
              [5, 6, 0, 8],
              [0, 0, 0, 0],
              [13, 14, 0, 16]]
        self.assertEqual(zeroMatrix(m1), m2)
        m1 = [[0, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
        m2 = [[0, 0, 0, 0],
              [0, 6, 7, 8],
              [0, 10, 11, 12],
              [0, 14, 15, 16]]
        self.assertEqual(zeroMatrix(m1), m2)
        m1 = [[1, 2, 3, 4],
              [5, 0, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
        m2 = [[1, 0, 3, 4],
              [0, 0, 0, 0],
              [9, 0, 11, 12],
              [13, 0, 15, 16]]
        self.assertEqual(zeroMatrix(m1), m2)
        m1 = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 0, 16]]
        m2 = [[1, 2, 0, 4],
              [5, 6, 0, 8],
              [9, 10, 0, 12],
              [0, 0, 0, 0]]
        self.assertEqual(zeroMatrix(m1), m2)
        m1 = [[1, 2, 3, 0],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
        m2 = [[0, 0, 0, 0],
              [5, 6, 7, 0],
              [9, 10, 11, 0],
              [13, 14, 15, 0]]
        self.assertEqual(zeroMatrix(m1), m2)





if __name__ == '__main__':
    unittest.main()


