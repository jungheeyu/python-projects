from art import logo
import os

clear = lambda: os.system('clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

# 'n': rerun calculator
def calculator():
    clear()
    print(logo)
    while True:
        num1 = input("What's the first number? ")
        if num1.isnumeric():
            num1 = float(num1)
            break

    for oper in operations:
        print(oper)

    # 'y': keep running calculator
    done = False
    while not done:
        while True:
            operation = input("Pick an operation: ")
            if operation in "+-*/":
                break
        
        while True:
            num2 = input("What's the next number? ")
            if num2.isnumeric():
                num2 = float(num2)
                break
        
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        next_order = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, \nor type 'e' to exit: ")
        if next_order  == 'y':
            num1 = answer   
        else:
            done = True
            if next_order  == 'e':
                print("Good bye!")
            else:
                calculator()

calculator()
