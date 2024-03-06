from calculator import evaluate_expression
from calculator_VectorNumber import calculate_expressionVectorNumber

expression = input("Введите выражение: ")
result = calculate_expressionVectorNumber(expression)
print("Результат:{",result,"}")
