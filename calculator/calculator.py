'''
Этот код сначала определяет функцию precedence, которая возвращает приоритет оператора. Затем определяется функция apply_operator, которая выполняет операцию над двумя значениями и одним оператором. Затем определяется функция evaluate_expression, которая принимает строку выражения и возвращает результат его вычисления.

После этого пользователь вводит выражение, оно передается функции evaluate_expression, которая вычисляет результат и выводит его на экран.
'''
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def apply_operator(operators, values):
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
        values.append(left // right)
    elif operator == '^':
        values.append(left ** right)

def evaluate_expression(expression):
    tokens = expression.replace(" ", "")
    values = []
    operators = []
    i = 0
    while i < len(tokens):
        if tokens[i] == '(':
            operators.append(tokens[i])
        elif tokens[i].isdigit():
            j = i
            while j < len(tokens) and (tokens[j].isdigit() or tokens[j] == '.'):
                j += 1
            values.append(int(tokens[i:j]))
            i = j - 1
        elif tokens[i] == ')':
            while operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
        else:
            while operators and precedence(operators[-1]) >= precedence(tokens[i]):
                apply_operator(operators, values)
            operators.append(tokens[i])
        i += 1
    while operators:
        apply_operator(operators, values)
    return values[-1]

expression = input("Введите выражение: ")
result = evaluate_expression(expression)
print("Результат:", result)