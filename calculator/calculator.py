import re

from Vector import Vector
from VectorException import VectorException


def precedence(op: str) -> int:
    """
    Возвращает приоритет оператора
    :param op: арифметический оператор
    :return: приоритет оператора
    """
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0


def apply_operator(operators: list, values: list) -> None:
    """
    Выполняет арифметическую операцию
    :param operators: список операторов
    :param values: список значений
    """
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    if operator == '+':
        values.append(left + right)
    elif operator == '-':
        values.append(left - right)
    elif operator == '*':
        values.append(left * right)
    elif operator == '/':
        if isinstance(left, Vector) or isinstance(right, Vector):
            values.append(left / right)
        else:
            if right == 0:
                raise ZeroDivisionError("Ошибка. Происходит деление на 0")
            values.append(int(left / right))
    elif operator == '^':
        if isinstance(left, Vector) or isinstance(right, Vector):
            values.append(left ** right)
        else:
            values.append(int(left ** right))


def evaluate_expression(expression: str):
    """
    Вычисляет выражение
    :param expression: выражение
    :return: результат выражения
    """
    try:
        expression = re.sub(r'\s+', ' ', expression)
        tokens = expression.split(" ")
        values = []
        operators = []

        for token in tokens:
            if token == '(':
                operators.append(token)

            elif token.isdigit() or (token.startswith('-') and token[1:].isdigit()):  # считываем число целиком
                values.append(int(token))

            elif token[0] == '{':
                values.append(parse_vector(token))

            elif token == ')':
                while operators[-1] != '(':  # пока не найдем ( выполняем операции
                    apply_operator(operators, values)
                operators.pop()

            else:
                while operators and precedence(operators[-1]) >= precedence(token):  # для приоритета
                    apply_operator(operators, values)
                operators.append(token)

        while operators:
            apply_operator(operators, values)

        return values[-1]

    except (ZeroDivisionError, VectorException) as e:
        return str(e)
    except:
        return "Ошибка при вычислении выражения"


def parse_vector(vector: str) -> Vector:
    if vector == '{}':
        raise VectorException("Вектор не может быть пустым")

    components = vector[1:-1].split(';')
    arguments = []
    for component in components:
        try:
            arguments.append(int(component))
        except ValueError:
            raise VectorException(f"Неверный формат ввода '{component}'")
    return Vector(*arguments)
