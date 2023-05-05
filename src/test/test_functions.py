from src.support_functions import get_digit, get_digits, get_difference_of_two_digits, get_num_len


class TestFunctions:

    def test_get_digit(self):
        assert get_digit(36, 0) == 6
        assert get_digit(36, 1) == 3
        assert get_digit(36, 2) == 0

    def test_get_digits(self):
        assert get_digits(36) == [3, 6]
        assert get_digits(100) == [1, 0, 0]
        assert get_digits(36436) == [3, 6, 4, 3, 6]

    def test_get_difference_of_two_digits(self):
        assert get_difference_of_two_digits(36) == 3
        assert get_difference_of_two_digits(16) == 5
        assert get_difference_of_two_digits(66) == 0

    def test_get_num_len(self):
        for num in range(10):
            assert get_num_len(num) == 1

        for num in range(10, 100):
            assert get_num_len(num) == 2

        for num in range(100, 1000):
            assert get_num_len(num) == 3

        for num in range(-9, 1):
            assert get_num_len(num) == 1

        for num in range(-99, -9):
            assert get_num_len(num) == 2

        for num in range(-999, -99):
            assert get_num_len(num) == 3

