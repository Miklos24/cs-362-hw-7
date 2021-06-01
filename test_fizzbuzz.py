from fizzbuzz import fizzbuzz
import unittest

class TestFizzbuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz()[2], 'Fizz')
    
    def test_buzz(self):
        self.assertEqual(fizzbuzz()[4], 'Buzz')

if __name__ == '__main__':
    unittest.main()