# Teddy Muli Ndaisi  SCT211-0023/2022

class Calculator:
    def __init__(self):
        pass

    def add (self, x, y):
        return x + y
    
    def substract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            result = "Can't divide by zero"
        return result
    
def menu():
    user_input = input("Enter first number, an operator(+, -, *, /) and the second number > ")
    while True:
        if '+' in user_input:
            operator = '+'
            break
        elif '-' in user_input:
            operator = '-'
            break
        elif '/' in user_input:
            operator = '/'
            break
        elif '*' in user_input:
            operator = '*'
            break
        else:
            user_input = input("Enter valid input")

    num1 = user_input.split(operator)
    num1 = num1[0]
    num1 = num1.strip()


    while True:
        try:
            num1 = int(num1)
            break
        except ValueError:
            num1 = input("Enter a valid first number")
    
    num2 = user_input.split(operator)[1].strip()
    while True:
        try:
            num2 = int(num2)
            break
        except ValueError:
            num2 = input("Enter a valid seconf number")

    input_list = [num1, num2, operator]
    return input_list

values = menu()
calculato_r = Calculator()

match values[2]:
    case '+':
        print(calculato_r.add(values[0], values[1]))
    case '-':
        print(calculato_r.substract(values[0], values[1]))
    case '*':
        print(calculato_r.multiply(values[0], values[1]))
    case '/':
        print(calculato_r.divide(values[0], values[1]))