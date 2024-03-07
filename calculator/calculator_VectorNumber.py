'''
    Функция extract_value_vector,принимает строку s и возвращает выражение перед оператором ,
    вектор после него  и операцию выражения.(все в виде строки)

    Функция calculate_VectorNumber, принимает на вход выражение, разбивает его на три части с помощью функции extract_value_vector,
    далее проводит опрецию между числом и вектором и возвращает результат в виде вектора
    
    Функция calculate_ExpressionVector, принимает на вход выражение,которое состоит из выражение и вектора, в
    результате вычисления возвращете вектор. 

'''
from  calculator import apply_operator,evaluate_expression

def extract_value_vector(expression):
    operators = ["+", "-", "/", "*", "^"]
    line = expression.replace(" ", "")
    brace_index = line.rfind('{')
    if brace_index == -1  or brace_index == 0  or line.count('{') != line.count('}') or line[brace_index - 1] not in operators:
        raise ValueError("Недопустимый формат выражения")  
    operator = line[brace_index - 1]
    value = line[:brace_index - 1]
    vector = line[brace_index:]
    return value, vector,operator

def calculate_VectorNumber(expression):
    try:
        value, vector, operator = extract_value_vector(expression)
        if vector.count('{') > 1 or vector.count('}') > 1:
            raise ValueError("Недопустимое количество фигурных скобок в векторе")  
        
        if not vector[1:-1].replace(',', '').replace(' ', '').isdigit():
            raise ValueError("Недопустимые символы в векторе")  
        
        if vector[1] == ',' or vector[-2] == ',':
            raise ValueError("Недопустимый формат в векторе")  
        if not( value.isdigit()):
            raise ValueError("Недопустимый формат выражения")
        
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
        return result
    
    except ValueError as e:
        return str(e)
    except:
        return "Ошибка при вычислении выражения"

def calculate_ExpressionVector(expression):
    try:
        part_expression, vector, operator = extract_value_vector(expression)
        if not( part_expression.isdigit()):
            raise ValueError("Недопустимый формат выражения")
        value = evaluate_expression(part_expression)
        return calculate_VectorNumber(str(value) + operator + vector)
    
    except ValueError as e:
        return str(e)    
    except:
        return "Некорректное выражение"