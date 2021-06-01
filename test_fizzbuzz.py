from fizzbuzz import fizzbuzz
import unittest

class TestFizzbuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz()[2], 'Fizz')
    
    def test_buzz(self):
        self.assertEqual(fizzbuzz()[4], 'Buzz')
    
    def test_range(self):
        self.assertEqual(len(fizzbuzz()), 100)

if __name__ == '__main__':
    unittest.main()