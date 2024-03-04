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
        if right == 0:
            raise ZeroDivisionError("Ошибка. Происходит деление на 0")
        values.append(left // right)
    elif operator == '^':
        values.append(left ** right)


def evaluate_expression(expression: str):
    """
    Вычисляет выражение
    :param expression: выражение
    :return: результат выражения
    """
    try:
        tokens = expression.replace(" ", "")
        values = []
        operators = []
        i = 0
        while i < len(tokens):
            # print("values:",values,"operators",operators, "i:",i, "tokens:", tokens )
            if tokens[i] == '(':
                operators.append(tokens[i])
            elif tokens[i].isdigit():  # считываем число целиком
                j = i
                while j < len(tokens) and (tokens[j].isdigit()):
                    j += 1
                values.append(int(tokens[i:j]))
                i = j - 1
            elif tokens[i] == ')':
                while operators[-1] != '(':  # пока не найдем ( выполняем операции
                    apply_operator(operators, values)
                operators.pop()
            else:
                while operators and precedence(operators[-1]) >= precedence(tokens[i]):  # для приоритета
                    apply_operator(operators, values)
                operators.append(tokens[i])
            i += 1
        while operators:
            apply_operator(operators, values)
        return values[-1]
    except ZeroDivisionError as e:
        return str(e)
    except:
        return "Ошибка при вычислении выражения"
