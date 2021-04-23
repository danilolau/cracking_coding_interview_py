from array import array
import unittest

def string_compression(string):
    char_array = array('u')
    char_t = string[0]
    count = 1
    for char in string[1:]:
        if char_t == char:
            count += 1
        else:
            add_string(char_array,char_t,count)
            char_t = char
            count = 1
    add_string(char_array,char_t,count)
    return ''.join(char_array)

def add_string(char_array, char, count):
    char_array.append(char)
    if count > 1:
        char_array.append(str(count))


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2bc5a3'),
        ('abcdef', 'abcdef'),
        
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()