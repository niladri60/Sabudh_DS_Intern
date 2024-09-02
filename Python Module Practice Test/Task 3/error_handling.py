# Define the custom exception class for handling negative numbers
class NegativeNumberError(Exception):
    # Custom exception to be raised when a negative number is encountered.
    pass

def main():
    try:
        # Prompt user to enter two numbers
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # Check if any number is negative and raise NegativeNumberError if so
        if num1 < 0 or num2 < 0:
            raise NegativeNumberError("Negative numbers are not allowed.")

        # Perform division
        result = num1 / num2

    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Cannot divide by zero.")

    except NegativeNumberError as e:
        # Handle custom negative number error
        print(f"Error: {e}")

    except ValueError:
        # Handle non-integer input error
        print("Error: Please enter valid integers.")

    else:
        # If no exceptions occur, print the result
        print(f"The result of dividing {num1} by {num2} is: {result}")

    finally:
        # This block always executes, indicating the end of the program
        print("Program execution completed.")

if __name__ == "__main__":
    main()
