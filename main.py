def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the operation (1/2/3/4): ")
    
    if operation == '1' or operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}.")
    elif operation == '2' or operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}.")
    elif operation == '3' or operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}.")
    elif operation == '4' or operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}.")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please choose a valid operation (1/2/3/4).")

if __name__ == "__main__":
    main()
