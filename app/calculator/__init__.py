""" 
This file is the "app/calculator.py" file. It contains a simple calculator that can add, subtract, multiply, 
and divide numbers based on what the user types.
"""

# First, we need to get some functions that can actually do the math for us. These functions (addition, 
# subtraction, multiplication, and division) are in another file called "operations.py" in the "app" folder.
# This is like opening a toolbox and pulling out the tools we need to do our math.
from app.operations import Operations
from typing import List
from app.calculation import Calculation, CalculationFactory
import sys

def display_history(history: List[Calculation]) -> None:
    """
    Displays the history of calculations performed during the session.

    Parameters:
        history (List[Calculation]): A list of Calculation objects representing past calculations.
    """
    if not history:
        print("You haven't done anything yet.")
    else:
        print("Calculation History:")
        for idx, calculation in enumerate(history, start=1):
            print(f"{idx}. {calculation}")


def display_help() -> None:
    """
    Displays the help message with usage instructions and supported operations.
    """
    help_message = """
Calculator REPL Help
--------------------
Usage:
    <operation> <number1> <number2>
    - Perform a calculation with the specified operation and two numbers.
    - Supported operations:
        add       : Adds two numbers.
        subtract  : Subtracts the second number from the first.
        multiply  : Multiplies two numbers.
        divide    : Divides the first number by the second.
        power     : exponentiates first number by second number.
        modulo    : Divides the first number by the second number and determines the remainder.

Special Commands:
    help      : Display this help message.
    history   : Show the history of calculations.
    exit      : Exit the calculator.

Examples:
    add 10 5
    subtract 15.5 3.2
    multiply 7 8
    divide 20 4
    """
    print(help_message)
# Now we're going to create the main function called "calculator". 
# A function is just a block of code that does something when you call it, kind of like a recipe that tells the 
# computer what to do.
def calculator():
    """Basic REPL calculator that performs addition, subtraction, multiplication, and division."""
    history: List[Calculation] = []
    # First, we print a message to welcome the user to the calculator.
    print("Welcome to the calculator REPL! Type 'exit' to quit, and help for other basic commands and assistance")
    
    
    # This is the part where the calculator keeps running. The 'while True' means we are going to keep 
    # doing something (in this case, asking the user for input) until we tell it to stop.
    while True:
        try:
            # Now we ask the user to type something, like "add 5 3". 
            # This will get the operation (like "add") and two numbers from the user.
            user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: ")
            if not user_input:
                continue
            user_input=user_input.lower()
            # This part checks if the user typed "exit". If they did, we print a message and stop the calculator.
            if user_input == "exit":
                print("Exiting calculator...")
                sys.exit(0)  # This "break" command tells the program to stop running the loop and exit.
            if user_input == "help":
                display_help()
                continue
            if user_input=="history":
                display_history(history)
                continue
            try:
                # Now we split the input into three parts: the operation (add, subtract, etc.) and the two numbers.
                operation, num1, num2 = user_input.split()
                # We have to make sure the numbers are actually numbers, so we convert them to floats.
                num1, num2 = float(num1), float(num2)
            except ValueError:
                # If the user doesn't type something correctly, like typing letters where numbers should be, we show an error.
                print("Invalid input. Please follow the format: <operation> <num1> <num2>. you can type help for more information on how to use this basic calulator")
                continue  # This "continue" means: try again by going back to the top of the loop.
            try:
                calculation = CalculationFactory.create_calculation(operation, num1, num2)
            except ValueError as ve:
                    # Handle unsupported operations
                    print(ve)
                    print("Type 'help' to see the list of supported operations.\n")
                    continue  # Prompt the user again
            try:
                result = calculation.execute()
            except ZeroDivisionError:
                # Handle division by zero specifically
                print("Can't Divide By Zero.")
                print("Please enter a non-zero divisor.\n")
                continue  # Prompt the user again
            except Exception as e:
                # Handle any other unforeseen exceptions
                print(f"An error occurred during calculation: {e}")
                print("Please try again.\n")
                continue  # Prompt the user again

            # Prepare the result string for display
            result_str: str = f"{calculation}"
            print(f"Result: {result_str}\n")

            # Append the calculation object to history
            history.append(calculation)
            # Finally, we print the result of the operation (for example, "Result: 8").
            print(f"Result: {result}")
        except KeyboardInterrupt:
            # EAFP example for handling unexpected interruption
            # Instead of checking if the user pressed Ctrl+C before each input,
            # we handle the KeyboardInterrupt exception.
            print("\nKeyboard interrupt detected. Exiting calculator. Goodbye!")
            sys.exit(0)
        except EOFError:
            # EAFP example for handling EOF (Ctrl+D)
            # Similar to KeyboardInterrupt, we handle the EOFError exception.
            print("\nEOF detected. Exiting calculator. Goodbye!")
            sys.exit(0)


# Explanation of __init__.py:
# In Python, a file named "__init__.py" is really important. It tells Python that the folder it's in (in this case, "calculator") 
# is a special kind of folder called a "package". Think of a package like a folder that contains related code, like a toolbox with
# different tools inside.
# 
# Without the "__init__.py" file, Python won't know that the folder can be used to group code together. It’s like a flag that says,
# "Hey Python, this folder can be used to import code!"
# 
# For example, if we put the "__init__.py" file in the "calculator" folder, we can import anything inside it by saying something like:
# "from app.calculator import calculator". The "__init__.py" file can be empty, or it can have code in it, but its main job is just 
# to make the folder a package.
