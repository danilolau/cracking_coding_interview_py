import unittest

def is_substring(str1,str2):
    is_sub = False
    if str1.find(str2) >= 0:
        is_sub = True
    return is_sub

def string_rotation(str1,str2):
    is_rotation = False
    if len(str1)==len(str2):
        is_rotation = is_substring(str1*2,str2)
    return is_rotation

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
