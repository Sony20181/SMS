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
        self.assertEqual(evaluate_expression('( 2 + 2 ) * 2'), 8)
        self.assertEqual(evaluate_expression('3 * 0'), 0)
        self.assertEqual(evaluate_expression('3 *     0'), 0)  # лишние пробелы - не проблема
        self.assertEqual(evaluate_expression('2 ^ 2'), 4)
        self.assertEqual(evaluate_expression('2 ^ ( 2 + 1 )'), 8)
        self.assertEqual(evaluate_expression('2 ^ ( 2 ^ 3 )'), 256)
        self.assertEqual(evaluate_expression('2 ^ 2 ^ 3'), 64)
        self.assertEqual(evaluate_expression('2 / 1'), 2)
        self.assertEqual(evaluate_expression('2 / 3'), 0)
        self.assertEqual(evaluate_expression('2 / 3'), 0)

        self.assertEqual(evaluate_expression('3 / 0'), "Ошибка. Происходит деление на 0")
        self.assertEqual(evaluate_expression('( 3 + 0 ) / 0'), "Ошибка. Происходит деление на 0")
        self.assertEqual(evaluate_expression('( 3 + 1 ) / ( 2 - 2 )'), "Ошибка. Происходит деление на 0")

        self.assertEqual(evaluate_expression('( 3 * 0'), "Ошибка при вычислении выражения")
        self.assertEqual(evaluate_expression('3 * 0 )'), "Ошибка при вычислении выражения")
        self.assertEqual(evaluate_expression('( 3 * 2 ) )'), "Ошибка при вычислении выражения")
        self.assertEqual(evaluate_expression('любой 123 текст'), "Ошибка при вычислении выражения")
        self.assertEqual(evaluate_expression('( 3 * 2 )'), 6)

    def test_Negative_expression(self):
        self.assertEqual(evaluate_expression('-2 ^ ( 2 + 3 )'), -32)
        self.assertEqual(evaluate_expression('-2 ^ -3'), 0)
        self.assertEqual(evaluate_expression('18 / -10'), -1)
        self.assertEqual(evaluate_expression('2 * -3 - 5'), -11)
        self.assertEqual(evaluate_expression('6 / -3 - 5 + -2'), -9)
        self.assertEqual(evaluate_expression('-10 * -10 / 9'), 11)
        self.assertEqual(evaluate_expression('5-10'), "Ошибка при вычислении выражения")

    def test_Vector_evaluate_expression(self):
        self.assertEqual(evaluate_expression('{}'), "Вектор не может быть пустым")
        self.assertEqual(evaluate_expression('{23;23;;}'), "Неверный формат ввода ''")
        self.assertEqual(evaluate_expression('{-91;78;3} - {3;1;0}'), '{-94;77;3}')
        self.assertEqual(evaluate_expression('{-1;-2;-3} + {3;1;0}'), '{2;-1;-3}')
        self.assertEqual(evaluate_expression('{1;2;3} * {3;1;0}'), 5)

        self.assertEqual(evaluate_expression('{-91;78;3} - 1000'), '{-1091;-922;-997}')
        self.assertEqual(evaluate_expression('{1;2;3} + 34'), '{35;36;37}')
        self.assertEqual(evaluate_expression('6 * {1;2;3} * 6'), '{36;72;108}')

        self.assertEqual(evaluate_expression('2 ^ ( 2 ^ 3 ) - {-1;-2;-3}'), '{-257;-258;-259}')
        self.assertEqual(evaluate_expression('{3;3;3} * {3;3;3} + {3;3;3}'), '{30;30;30}')
        self.assertEqual(
            evaluate_expression('( -3 * ( 16 ^ 2 - 34 * 3 ) + 2 ^ ( 2 ^ 3 ) ) - {9;78992;309} * {32;23;23}'), -1824417)

    def test_Vector_Error(self):
        self.assertEqual(evaluate_expression('{6;3;5} - {3;2;3;1;1}'), "У векторов разные размерности")
        self.assertEqual(evaluate_expression('{6;3;5} * {3}'), "У векторов разные размерности")
        self.assertEqual(evaluate_expression('12 / {1;2;3}'), 'Ошибка при вычислении выражения')
        self.assertEqual(evaluate_expression('{-1;-2;-3} ^ {3;1;0}'), 'Невозможно возвести вектор в степень')
        self.assertEqual(evaluate_expression('{-1;-2;-3} / {3;1;1}'), 'Ошибка при вычислении выражения')

        self.assertEqual(evaluate_expression('{}'), 'Вектор не может быть пустым')
        self.assertEqual(evaluate_expression('{23;23;;}'), "Неверный формат ввода ''")
        self.assertEqual(evaluate_expression('{dsdsds}'), "Неверный формат ввода 'dsdsds'")
