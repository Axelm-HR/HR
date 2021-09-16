class Calculator:
    def __init__(self):
        pass

    def addition(self, x, y):
        return x + y
    
    def subtraction(self, x, y):
        return x - y
    
    def multiplication(self, x, y):
        return x * y
    
    def division(self, x, y):
        return x / y
    

calc = Calculator()
equation = input("Enter an equation: ").split(' ')

while equation[0].lower() != "q":
    try:
        if equation[1] == "+":
            print(f"Result: {calc.addition(int(equation[0]), int(equation[2])):.2f}")
        elif equation[1] == "-":
            print(f"Result: {calc.subtraction(int(equation[0]), int(equation[2])):.2f}")
        elif equation[1] == "*":
            print(f"Result: {calc.multiplication(int(equation[0]), int(equation[2])):.2f}")
        elif equation[1] == "/":
            print(f"Result: {calc.division(int(equation[0]), int(equation[2])):.2f}")
        elif equation[1] != "+" or equation[1] != "-" or equation[1] != "*" or equation[1] != "/":
            print("Invalid operator")
        equation = input("Enter an equation: ").split(' ')
    except ZeroDivisionError:
        print("Can't divide by 0")
        equation = input("Enter an equation: ").split(' ')
    except ValueError:
        print("Invalid operands")
        equation = input("Enter an equation: ").split(' ')