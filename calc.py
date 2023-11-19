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
            successful = False
            while not successful:
                num1 = input("Enter number: ")
                try:
                    num1 = int(num1)
                except:
                    try:
                        num1 = float(num1)
                    except:
                        num1 = input("Please enter a number\n\nEnter number: ")
                    else:
                        successful = True
                else:
                    successful = True
        else:
            successful = False
            while not successful:
                num1 = input("Enter first number: ")
                try:
                    num1 = int(num1)
                except:
                    try:
                        num1 = float(num1)
                    except:
                        num1 = input("Please enter a number\n\nEnter first number: ")
                    else:
                        successful = True
                else:
                    successful = True
            successful = False
            while not successful:
                num2 = input("Enter second number: ")
                try:
                    num2 = int(num2)
                except:
                    try:
                        num2 = float(num2)
                    except:
                        num2 = input("Please enter a number\n\nEnter second number: ")
                    else:
                        successful = True
                else:
                    successful = True

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
        base = 0
        successful = False
        while not successful:
            base = input("Enter the base: ")
            try:
                base = int(base)
            except:
                try:
                    base = float(base)
                except:
                    base = input("Please enter a number\n\nEnter the base: ")
                else:
                    successful = True
            else:
                successful = True
        print(f"Logarithm base {base} of {num1} = {logarithm(num1, base)}")
    elif choice in ('8', '9', '10'):
        angle = 0
        successful = False
        while not successful:
            angle = input("Enter angle in degrees: ")
            try:
                angle = int(angle)
            except:
                try:
                    angle = float(angle)
                except:
                    angle = input("Please enter a number\n\nEnter angle in degrees: ")
                else:
                    successful = True
            else:
                successful = True
        if choice == '8':
            print(f"sin({angle}) = {trigonometric_operation(angle, 'sin')}")
        elif choice == '9':
            print(f"cos({angle}) = {trigonometric_operation(angle, 'cos')}")
        else:
            print(f"tan({angle}) = {trigonometric_operation(angle, 'tan')}")
    elif choice == '11':
        successful = False
        while not successful:
            num1 = input("Enter the exponent: ")
            try:
                num1 = int(num1)
            except:
                try:
                    num1 = float(num1)
                except:
                    num1 = input("Please enter a number\n\nEnter the exponent: ")
                else:
                    successful = True
            else:
                successful = True
        print(f"e^{num1} = {exponential_function(num1)}")
    elif choice == '12':
        num_base = 0
        successful = False
        while not successful:
            num_base = input("Enter the num_base: ")
            try:
                num_base = int(num_base)
            except:
                try:
                    num_base = float(num_base)
                except:
                    num_base = input("Please enter a number\n\nEnter the num_base: ")
                else:
                    successful = True
            else:
                successful = True
        successful = False
        while not successful:
            num1 = input("Enter the exponent: ")
            try:
                num1 = int(num1)
            except:
                try:
                    num1 = float(num1)
                except:
                    num1 = input("Please enter a number\n\nEnter the exponent: ")
                else:
                    successful = True
            else:
                successful = True
        print(f"{num_base}^^{num1} = {tetration(num_base, num1)}")
    elif choice == '13':
        print("Exiting the calculator. Goodbye!")
    else:
        print("Invalid input. Please enter a number between 1 and 13.")

    choice = input("Do you want to continue calculating? (Y, N): ").lower().strip()
    while choice not in ('y', 'n'):
        choice = input("Do you want to continue calculating? (Y, N): ").lower().strip()
    if choice == "y":
        calculator()

if __name__ == "__main__":
    calculator()
