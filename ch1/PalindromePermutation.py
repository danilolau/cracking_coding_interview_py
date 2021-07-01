from collections import Counter
import unittest

def pal_perm(s: str):
    fs = "".join(filter(lambda x: x >= "a" and x <= "z",s.lower()))
    counter = Counter(fs)
    odds = 0
    is_pal = True

    for count in counter.values():
        if count%2 == 1:
            odds += 1

    if odds > 1:
        is_pal = False

    return is_pal

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
        ('aziZ', False)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()