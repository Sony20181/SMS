import unittest

from calculator import precedence, evaluate_expression


class TestCalculator(unittest.TestCase):

    def test_precedence(self):
        self.assertEqual(precedence('+'), 1)
        self.assertEqual(precedence('-'), 1)
        self.assertEqual(precedence('*'), 2)
        self.assertEqual(precedence('/'), 2)
        self.assertEqual(precedence('^'), 3)
        self.assertEqual(precedence('//'), 0)

    def test_evaluate_expression(self):
        self.assertEqual(evaluate_expression('1 + 1'), 2)
        self.assertEqual(evaluate_expression('1 - 1'), 0)
        self.assertEqual(evaluate_expression('2 + 2 * 2'), 6)
        self.assertEqual(evaluate_expression('(2 + 2) * 2'), 8)
        self.assertEqual(evaluate_expression('3 * 0'), 0)
        self.assertEqual(evaluate_expression('3 *     0'), 0)  # лишние пробелы - не проблема
        self.assertEqual(evaluate_expression('2^2'), 4)
        self.assertEqual(evaluate_expression('2 ^(2 + 1)'), 8)
        self.assertEqual(evaluate_expression('2 ^ (2 ^ 3)'), 256)
        self.assertEqual(evaluate_expression('2 ^ 2 ^ 3'), 64)
        self.assertEqual(evaluate_expression('2 / 1'), 2)
        self.assertEqual(evaluate_expression('2 / 3'), 0)
        self.assertEqual(evaluate_expression('2 / 3'), 0)

        self.assertEqual(evaluate_expression('3 / 0'), "Ошибка. Происходит деление на 0")
        self.assertEqual(evaluate_expression('(3 + 0) / 0'), "Ошибка. Происходит деление на 0")
        self.assertEqual(evaluate_expression('(3 + 1) / (2 - 2)'), "Ошибка. Происходит деление на 0")

        self.assertEqual(evaluate_expression('(3 * 0'), "Ошибка при вычислении выражения")
        self.assertEqual(evaluate_expression('3 * 0)'), "Ошибка при вычислении выражения")
        self.assertEqual(evaluate_expression('(3 * 2))'), "Ошибка при вычислении выражения")
        self.assertEqual(evaluate_expression('любой 123 текст'), "Ошибка при вычислении выражения")
        self.assertEqual(evaluate_expression('(3 * 2)'), 6)
