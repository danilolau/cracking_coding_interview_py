from collections import Counter
import unittest

def pal_perm(string):
    counter = Counter()
    i = 0
    string = string.lower()
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            counter[char] += 1
            i += 1
    i = i%2
    for key in counter:
        if counter[key]%2 != 0 and i==0:
            return False
        elif counter[key]%2 != 0 and i==1:
            i = 0
    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()