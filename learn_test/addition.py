import unittest

from learn_test import addition_of_numbers


class TestAddition(unittest.TestCase):

    def test_addition_of_two_numbers(self):
        add = addition_of_numbers.add_numbers(3, 3)
        self.assertEqual(6, addition_of_numbers.add())
