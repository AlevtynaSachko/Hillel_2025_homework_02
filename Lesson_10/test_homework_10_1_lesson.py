import pytest
#6.2
from test_functions_10 import contains_h, filter_strings_only, sum_even_numbers, add_numbers, average, longest_word

class TestContainsH:

    def test_contains_lowercase_h(self):
        assert contains_h("hello") is True

    def test_contains_uppercase_h(self):
        assert contains_h("Hello") is True

    def test_contains_missing(self):
        assert contains_h("world") is False


#6.3

class TestFilterStringsOnly:

    def test_mixed_list(self):
        assert filter_strings_only([1, "hello", 3.14, "world", True]) == ["hello", "world"]

    def test_all_strings(self):
        assert filter_strings_only(["a", "b", "c"]) == ["a", "b", "c"]

    def test_no_strings(self):
        assert filter_strings_only([1, 2, 3, None, False]) == []


#6.4

class TestSumEvenNumbers:

        def test_mixed_numbers(self):
            assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12  # 2 + 4 + 6

        def test_all_even(self):
            assert sum_even_numbers([2, 4, 6, 8]) == 20

        def test_no_even(self):
            assert sum_even_numbers([1, 3, 5, 7]) == 0

        def test_empty_list(self):
            assert sum_even_numbers([]) == 0

        def test_negative_numbers(self):
            assert sum_even_numbers([-2, -3, -4]) == -6

        def test_zero_in_list(self):
            assert sum_even_numbers([0, 1, 2]) == 2  # 0 + 2


#7.1.2

class TestAddNumbers:

        def test_positive_numbers(self):
            assert add_numbers(3, 5) == 8

        def test_negative_numbers(self):
            assert add_numbers(-2, -4) == -6

        def test_mixed_sign_numbers(self):
            assert add_numbers(-3, 7) == 4

        def test_with_zero(self):
            assert add_numbers(0, 5) == 5
            assert add_numbers(5, 0) == 5

        def test_floats(self):
            assert add_numbers(2.5, 3.5) == 6.0


#7.1.3

class TestAverage:

        def test_positive_numbers(self):
            assert average([2, 4, 6, 8]) == 5.0

        def test_zero(self):
            assert average([0, 0, 0]) == 0.0

        def test_mixed_numbers(self):
            assert average([-3, 3, 9]) == 3.0

        def test_empty_list(self):
            assert average([]) == 0

        def test_one_element(self):
            assert average([10]) == 10.0


#7.1.5

class TestLongestWord:

    def test_typical_list(self):
        assert longest_word(["we", "are", "princes", "of", "universe"]) == "universe"

    def test_empty_list(self):
        assert longest_word([]) == ""

    def test_equal_length(self):
        result = longest_word(["ned", "tod", "rod"])
        assert result in ["ned", "tod", "rod"]

