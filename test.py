import unittest
from add import add


class AddTest(unittest.TestCase):
    """A test class for the `add` function.

    Attributes:
        None

    Methods:
        test_1_add_1: Tests the addition of two integers (1 + 1).
        test_str_add_str: Tests the addition of two strings ('1' + '-1').
    """

    def test_1_add_1(self):
        """Test the addition of two integers (1 + 1).

        This method asserts that the result of adding 1 and 1 using the
        `add` function is equal to 2.
        """
        self.assertEqual(add(1, 1), 2)

    def test_str_add_str(self):
        """Test the addition of two strings ('1' + '-1').

        This method asserts that the result of adding the strings '1' and
        '-1' using the `add` function is equal to 0.
        """
        self.assertEqual(add('1', '-1'), 0)


if __name__ == '__main__':
    unittest.main()
