def calculator():
    print("Welcome to the Enhanced Calculator!")
    print("Available operations:")
    print(" +  : Addition")
    print(" -  : Subtraction")
    print(" *  : Multiplication")
    print(" /  : Division")
    print(" %  : Modulus")
    print(" ** : Exponentiation")
    print(" // : Floor Division")

    while True:
        try:
            # Get first number
            num1 = float(input("\nEnter the first number: "))

            # Get operation
            operation = input("Enter an operation (+, -, *, /, %, **, //): ").strip()

            # Get second number
            num2 = float(input("Enter the second number: "))

            # Perform the operation
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    raise ZeroDivisionError("You can't divide by zero.")
                result = num1 / num2
            elif operation == '%':
                result = num1 % num2
            elif operation == '**':
                result = num1 ** num2
            elif operation == '//':
                if num2 == 0:
                    raise ZeroDivisionError("You can't divide by zero.")
                result = num1 // num2
            else:
                print("❌ Invalid operation. Please try again.")
                continue

            print(f"✅ Result: {num1} {operation} {num2} = {result}")

        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")
        except ZeroDivisionError as e:
            print(f"❌ Error: {e}")

        # Ask if user wants to calculate again
        again = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("👋 Thanks for using the calculator. Goodbye!")
            break

# Run the enhanced calculator
calculator()

