def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            return operation
        print("Invalid operation. Please enter one of +, -, *, /.")

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

def main():
    print("Welcome to the Python Calculator!")

    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        operation = get_operation()

        result = calculate(num1, num2, operation)
        print(f"Result: {result}")

        continue_calc = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_calc != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
