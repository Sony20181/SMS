'''
    Функция extract_value_vector,принимает строку s и возвращает выражение перед оператором ,
    вектор после него  и операцию выражения.(все в виде строки)

     Функция calculate_expressionVectorNumber, принимает на вход выражение, разбивает его на три части с помощью функции extract_value_vector,
     далее проводит опрецию между числом и вектором и возвращает результат в виде вектора

'''
from  calculator import apply_operator

def extract_value_vector(stroka):
    brace_index = stroka.rfind('{')
    
    if brace_index == -1:
        return None
    if brace_index == 0:
        return None
    operator = stroka[brace_index - 1]
   
    index = stroka.index(operator)
    value = stroka[:index]
    vector = stroka[index+1:]
    return value, vector,operator

def calculate_expressionVectorNumber(expression):
    tokens = expression.replace(" ", "")
    if (extract_value_vector(tokens) == None):
        return  expression
    
    value, vector, operator = extract_value_vector(tokens)
    Vector_list = list(map(int, vector[1 : -1].split(',')))

    values = []
    operators = []
    result = []
    for num in Vector_list:
        values.append(num)
        operators.append(operator)
        values.append(int(value))
        while len(operators) > 0 and len(values) > 1:
            k = apply_operator(operators, values)
            result.append(k[0])
            values = []
    print(value, vector,operator,Vector_list)
  
    return result
