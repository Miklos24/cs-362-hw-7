from fizzbuzz import fizzbuzz
import unittest

class TestFizzbuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz()[2], 'Fizz')

if __name__ == '__main__':
    unittest.main()