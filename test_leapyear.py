from leapyear import isLeapYear
import unittest

class TestLeapYear(unittest.TestCase):
    def test_year4(self):
        self.assertTrue(isLeapYear(4))

if __name__ == '__main__':
    unittest.main()