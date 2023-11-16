import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base):
    return math.log(x, base)

def trigonometric_operation(x, operation):
    if operation == 'sin':
        return math.sin(math.radians(x))
    elif operation == 'cos':
        return math.cos(math.radians(x))
    elif operation == 'tan':
        return math.tan(math.radians(x))
    else:
        return "Invalid trigonometric operation"

def exponential_function(x):
    return math.exp(x)

def tetration(b, n):
    if n == 1:
        return b
    else:
        return b ** tetration(b, n - 1)

def calculator():
    print("Welcome to the Inbuilt Calculator!")
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sin")
    print("9. Cos")
    print("10. Tan")
    print("11. Exponential")
    print("12. Tetration")
    print("13. Exit")

    choice = input("Enter choice (1-12): ")
    num1 = 0
    num2 = 0

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        if choice in ('6', '7'):
            num1 = float(input("Enter number: "))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print(f"{num1} ** {num2} = {power(num1, num2)}")
    elif choice == '6':
        print(f"Square root of {num1} = {square_root(num1)}")
    elif choice == '7':
        base = float(input("Enter the base: "))
        print(f"Logarithm base {base} of {num1} = {logarithm(num1, base)}")
    elif choice == '8':
        angle = float(input("Enter angle in degrees: "))
        print(f"sin({angle}) = {trigonometric_operation(angle, 'sin')}")
    elif choice == '9':
        angle = float(input("Enter angle in degrees: "))
        print(f"cos({angle}) = {trigonometric_operation(angle, 'cos')}")
    elif choice == '10':
        angle = float(input("Enter angle in degrees: "))
        print(f"tan({angle}) = {trigonometric_operation(angle, 'tan')}")
    elif choice == '11':
        num1 = float(input("Enter the exponent: "))
        print(f"e^{num1} = {exponential_function(num1)}")
    elif choice == '12':
        base = float(input("Enter the base: "))
        num1 = float(input("Enter the exponent: "))
        print(f"{base}^^{num1} = {tetration(base, num1)}")
    elif choice == '13':
        print("Exiting the calculator. Goodbye!")
    else:
        print("Invalid input. Please enter a number between 1 and 13.")

    choice = input("Do you want to continue calculating? (Y, N): ").lower().strip()
    while choice not in ('y', 'n'):
        choice = input("Do you want to continue calculating? (Y, N): ").lower().strip()
    if choice == "y":
        calculator()
