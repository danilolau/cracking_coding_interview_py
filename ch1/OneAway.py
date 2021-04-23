import unittest

def one_away(str1,str2):
    dif = len(str1)-len(str2)
    if dif == 0:
        return check_equal(str1,str2)
    elif dif == 1:
        return check_diff(str1,str2)
    elif dif == -1:
        return check_diff(str2,str1)
    else:
        return False

def check_equal(str1,str2):
    edit = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            edit += 1
            if edit > 1:
                return False
    return True

def check_diff(str1,str2):
    edit = 0
    i = 0
    while i < len(str2):
        if str1[i+edit]!=str2[i]:
            edit += 1
            if edit > 1:
                return False
            i -= 1
        i += 1
    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()