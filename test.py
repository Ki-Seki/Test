import unittest
from add import add

class addTest(unittest.TestCase):

    def test_1_add_1(self):
        self.assertEqual(add(1, 1), 2)

    def test_str_add_str(self):
        self.assertEqual(add('1', '-1'), 0)

if __name__ == '__main__':
    unittest.main()