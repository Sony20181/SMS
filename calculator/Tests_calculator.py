import unittest

from calculator import precedence


class TestCalculator(unittest.TestCase):

    def test_precedence(self):
        self.assertEqual(precedence('+'), 1)
        self.assertEqual(precedence('-'), 1)
        self.assertEqual(precedence('*'), 2)
        self.assertEqual(precedence('/'), 2)
        self.assertEqual(precedence('^'), 3)
        self.assertEqual(precedence('//'), 0)
