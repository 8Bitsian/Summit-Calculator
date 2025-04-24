# Imani Hollie 03/14/2025 @ 11:38 AM GTC
# A calculator that performs basic arithmetic, i.e., addition, subtraction, multiplication, and division

from decimal import Decimal, getcontext

# Define Addition() Function
def addition(a, b, points):
    # Set Precision for Intermediate Calculations
    getcontext().prec = points + 2 
    result = Decimal(a) + Decimal(b)
    return f"Result: {result:.{points}f}"

# Define Subtraction() Function
def subtraction(a, b, points):
    getcontext().prec = points + 2
    result = Decimal(a) - Decimal(b)
    return f"Result: {result:.{points}f}"

# Define Multiplication() Function
def multiplication(a, b, points):
    getcontext().prec = points + 2
    result = Decimal(a) * Decimal(b)
    return f"Result: {result:.{points}f}"

# Define Division() Function
def division(a, b, points):
    if b != 0:
        getcontext().prec = points + 2
        result = Decimal(a) / Decimal(b)
        return f"Result: {result:.{points}f}"
    else:
        return "ERROR: Division by Zero"

# Define Integer Division() Function
def int_division(a, b, points):
    if b != 0:
        getcontext().prec = points + 2
        result = Decimal(a) // Decimal(b)
        return f"Result: {result:.{points}f}"
    else:
        return "ERROR: Division by Zero"

# Define Print_Menu() Function
def print_menu():
    print("BASIC CALCULATOR")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Integer Division")
    print("H. View History")
    print("X. Exit Program")

# Create Main() Application Logic
def main():
    # Initialize History Array
    history = []

    # Operation Symbols Dictionary
    op_symbols = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
        "5": "//"
    }

    print_menu()

    while True:
        # Get User Input for Operation
        option = input("\nChoose Operation: ").lower()
        # Exit Condition = 'X'
        if option == 'x':
            print("Goodbye!")
            break
        elif option == 'h':
            print("\nCALCULATION HISTORY: ")
            for record in history:
                print(record)
            continue

        try:
            # Get User Input for Values
            num1 = float(input("Enter Value: "))
            num2 = float(input("Enter Value: "))
            points = int(input("Round To: "))

            if option == "1":
                # 1. Addition
                result = addition(num1, num2, points)
            elif option == "2":
                # 2. Subtraction
                result = subtraction(num1, num2, points)
            elif option == "3":
                # 3. Multiplication
                result = multiplication(num1, num2, points)
            elif option == "4":
                # 4. Division
                result = division(num1, num2, points)
            elif option == "5":
                # 5. Integer Division
                result = int_division(num1, num2, points)
            else:
                # ERROR Message
                print("ERROR: Invalid Input")
                continue

            print(result)
            history.append(f"{num1} {op_symbols[option]} {num2} = {result}")
            
        except ValueError:
            print("ERROR: Invalid Input")

if __name__ == "__main__":
    main()
