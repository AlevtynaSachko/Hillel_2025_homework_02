#тести для 6.2

import unittest
from homework_9_1_lesson import contains_h

class TestContainsH(unittest.TestCase):

    def test_contains_h_lowercase(self):
        self.assertTrue(contains_h("hididdly"))

    def test_contains_h_uppercase(self):
        self.assertTrue(contains_h("Hididdly"))

    def test_contains_h_missing(self):
        self.assertFalse(contains_h("okilydokily"))


#тести для 6.3

import unittest
from homework_9_1_lesson import filter_strings_only

class TestFilterStringsOnly(unittest.TestCase):
    def test_mixed_list(self):
        source = ['1', 2, 'three', 4.0, True, 'hello']
        result = filter_strings_only(source)
        expected = ['1', 'three', 'hello']
        self.assertEqual(result, expected)

    def test_all_strings(self):
        source = ['a', 'b', 'c']
        result = filter_strings_only(source)
        self.assertEqual(result, source)

    def test_no_strings(self):
        source = [1, 2, 3, True, None]
        result = filter_strings_only(source)
        self.assertEqual(result, [])



#тести для 6.4

import unittest
from homework_9_1_lesson import sum_even_numbers

class TestSumEvenNumbers(unittest.TestCase):

    def test_mixed_numbers(self):
        source = [10, 21, 33, 40, 55, 67, 77]
        expected = 50
        result = sum_even_numbers(source)
        self.assertEqual(result, expected)

    def test_all_even(self):
        source = [2, 4, 6, 8]
        expected = 20
        result = sum_even_numbers(source)
        self.assertEqual(result, expected)

    def test_no_even(self):
        source = [1, 3, 5, 7]
        expected = 0
        result = sum_even_numbers(source)
        self.assertEqual(result, expected)

#тести для 7.1 task 2

import unittest
from homework_9_1_lesson import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(add_numbers(7, 8), 15)

    def test_negative_and_positive(self):
        self.assertEqual(add_numbers(-5, 10), 5)

    def test_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)

    def test_floats(self):
        self.assertAlmostEqual(add_numbers(2.5, 3.1), 5.6)

    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-3, -7), -10)


#тести для 7.1 task 3

import unittest
from homework_9_1_lesson import average

class TestAverage(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(average([10, 20, 30]), 20)

    def test_single_value(self):
        self.assertEqual(average([7]), 7)

    def test_empty_list(self):
        self.assertEqual(average([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(average([-10, -20, -30]), -20)

    def test_mixed_positive_negative(self):
        self.assertEqual(average([-10, 0, 10]), 0)

    def test_with_floats(self):
        self.assertAlmostEqual(average([1.5, 2.5, 3.0]), 2.3333333333333335)

    def test_single_float_value(self):
        self.assertEqual(average([3.14]), 3.14)


#тести для 7.1 task 5

import unittest
from homework_9_1_lesson import longest_word

class TestLongestWord(unittest.TestCase):

    def test_typical_list(self):
        words = ["we", "are", "the", "champions"]
        expected = "champions"
        result = longest_word(words)
        self.assertEqual(result, expected)

    def test_empty_list(self):
        words = []
        expected = ""
        result = longest_word(words)
        self.assertEqual(result, expected)

    def test_equal_length_words(self):
        words = ["dog", "cat", "hat"]
        expected = "dog" # або перше з найдовших — залежить від реалізації
        result = longest_word(words)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)