import unittest
from src.lib.sample_lib import add_two_numbers

class SampleLibTest(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertTrue(add_two_numbers(10, 20) == (10 + 20), "Does not do what it says on the tin")


if __name__ == '__main__':
    unittest.main()