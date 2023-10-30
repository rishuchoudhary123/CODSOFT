
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter '0' to end the program")
    
    user_input = input(": ")
    
    if user_input == "0":
        break
    elif user_input in ["add", "subtract", "multiply", "divide"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if user_input == "+":
            print("Result:", add(num1, num2))
        elif user_input == "-":
            print("Result:", subtract(num1, num2))
        elif user_input == "*":
            print("Result:", multiply(num1, num2))
        elif user_input == "/":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")
