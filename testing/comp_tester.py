import unittest
from string_comparison import StringComparison as sc, StringComparisonError


class TestStringComparison(unittest.TestCase):

    # Example of Positive Test
    def test_compare_success(self):
        assert sc.compare("Mike", "mike")

    # def test_adder_success(self):
        # assert sc.adder(4, 9) == 11
    # Example of Negative Test
    def test_compare_failure(self):
        try:
            sc.compare("Mike", 4)
            raise AssertionError("Compare did not handle incorrect data types")
        except StringComparisonError as e:  # <- But if it does catch comparison error
            assert str(e) == "Name Does Not Match"

    # If you leave the test method empty it will make the test results passing
    def test_error(self):
        pass


if __name__ == '__main__':
    unittest.main()
