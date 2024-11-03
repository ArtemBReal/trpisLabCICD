def calculate(num1, num2, operation):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Деление на ноль запрещено"
    elif operation == '*':
        result = num1 * num2
    return result