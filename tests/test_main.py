import unittest
from src.main import my_function

class TestMain(unittest.TestCase):
    def test_my_function(self):
        # Test case 1
        result = my_function(5)
        self.assertEqual(result, 10)

        # Test case 2
        result = my_function(10)
        self.assertEqual(result, 20)

        # Test case 3
        result = my_function(0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()