# Simple Calculator in Python

# Function to perform the chosen operation
def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation!"

def show_menu():
    print("\nSimple Calculator Menu:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

def main():
    while True:
        # Display menu
        show_menu()

        # Take inputs
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("\nChoose the operation (1-4): ")

        # Perform calculation and display result
        result = calculate(num1, num2, operation)
        print(f"\nResult: {result}")

        # Ask user if they want to perform another calculation
        choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
