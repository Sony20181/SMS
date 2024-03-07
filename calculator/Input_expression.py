from calculator import evaluate_expression
from calculator_VectorNumber import calculate_VectorNumber, extract_value_vector,calculate_ExpressionVector

expression = input("Введите выражение: ")
result = calculate_ExpressionVector(expression)
#print("Результат:{",result,"}")
print("Результат:",result )
