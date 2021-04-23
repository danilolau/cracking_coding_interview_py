from array import array
import unittest

def urlify(string,length):
    char_array = array('u',string)
    dif = len(char_array) - length
    for i in reversed(range(length)):
        if char_array[i] == ' ':
            char_array[i+dif-2:i+dif+1] = array('u','%20')
            #char_array[i+dif-1] = '2'
            #char_array[i+dif-2] = '%'
            dif -= 2
        else:
            char_array[i+dif] = char_array[i]
    return ''.join(char_array)

class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        ('much ado about nothing      ', 22,
         'much%20ado%20about%20nothing'),
        ('Mr John Smith    ', 13, 'Mr%20John%20Smith')]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()