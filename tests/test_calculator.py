""" tests/test_calculator.py """
import sys
import pytest
from io import StringIO
from app.calculator import display_help, display_history, calculator
def test_display_help(capsys):
    """
    Test the display_help function to ensure it prints the correct help message.

    AAA Pattern:
    - Arrange: No special setup required for this function.
    - Act: Call the display_help function.
    - Assert: Capture the output and verify it matches the expected help message.
    """
    # Arrange
    # No arrangement needed since display_help doesn't require any input or setup.

    # Act
    display_help()

    # Assert
    # Capture the printed output
    captured = capsys.readouterr()
    expected_output = """
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
    power 2 4
    modulo 10 3
    """
    # Remove leading/trailing whitespace for comparison
    assert captured.out.strip() == expected_output.strip()

def test_display_history_empty(capsys):
    """
    Test the display_history function when the history is empty.

    AAA Pattern:
    - Arrange: Create an empty history list.
    - Act: Call the display_history function with the empty history.
    - Assert: Capture the output and verify it indicates no calculations have been performed.
    """
    # Arrange
    history = []

    # Act
    display_history(history)

    # Assert
    captured = capsys.readouterr()
    assert captured.out.strip() == "You haven't done anything yet."


def test_display_history_with_entries(capsys):
    # Arrange
    history = [
        "AddCalculation: 10.0 Add 5.0 = 15.0",
        "SubtractCalculation: 20.0 Subtract 3.0 = 17.0",
        "MultiplyCalculation: 7.0 Multiply 8.0 = 56.0",
        "DivideCalculation: 20.0 Divide 4.0 = 5.0",
        "ModuloCalculation: 10.0 Modulo 3.0 = 1.0",
        "PowerCalculation: 13.0 Power 4.0 = 28561.0",
    ]
    # Act
    display_history(history)
    # Assert
    captured = capsys.readouterr()
    expected_output = """Calculation History:
1. AddCalculation: 10.0 Add 5.0 = 15.0
2. SubtractCalculation: 20.0 Subtract 3.0 = 17.0
3. MultiplyCalculation: 7.0 Multiply 8.0 = 56.0
4. DivideCalculation: 20.0 Divide 4.0 = 5.0
5. ModuloCalculation: 10.0 Modulo 3.0 = 1.0
6. PowerCalculation: 13.0 Power 4.0 = 28561.0"""
    assert captured.out.strip() == expected_output.strip()

def test_calculator_exit(monkeypatch, capsys):
    """
    Test the calculator function's ability to handle the 'exit' command.

    AAA Pattern:
    - Arrange: Prepare the input 'exit' to simulate user typing 'exit'.
    - Act: Call the calculator function.
    - Assert: Verify that the calculator exits gracefully and prints the exit message.
    """
    # Arrange
    user_input = 'exit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()
    # Assert
    captured = capsys.readouterr()
    assert "Exiting calculator..." in captured.out
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 0  # Exit code 0 indicates a clean exit
def test_calculator_help_command(monkeypatch, capsys):
    """
    Test the calculator function's ability to handle the 'help' command.
    AAA Pattern:
    - Arrange: Prepare the input 'help' followed by 'exit' to simulate user interactions.
    - Act: Call the calculator function.
    - Assert: Verify that the help message is displayed and the calculator exits gracefully.
    """
    # Arrange
    user_input = 'help\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Asserts
    captured = capsys.readouterr()
    assert "Calculator REPL Help" in captured.out
    assert "Exiting calculator..." in captured.out
def test_calculator_history_command(monkeypatch, capsys):
    """
    Test the calculator function's ability to handle the 'help' command.
    AAA Pattern:
    - Arrange: Prepare the input 'help' followed by 'exit' to simulate user interactions.
    - Act: Call the calculator function.
    - Assert: Verify that the help message is displayed and the calculator exits gracefully.
    """
    # Arrange
    user_input = 'history\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Asserts
    captured = capsys.readouterr()
    assert "You haven't done anything yet" in captured.out
    assert "Exiting calculator..." in captured.out

def test_calculator_history(monkeypatch, capsys):
    """
    Test the calculator's ability to display calculation history.

    AAA Pattern:
    - Arrange: Prepare a sequence of operations followed by 'history' and 'exit'.
    - Act: Call the calculator function.
    - Assert: Verify that the history is displayed correctly.
    """
    # Arrange
    user_input = 'power 10 5\nadd 20 3\nhistory\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Result: PowerCalculation: 10.0 Power 5.0 = 100000.0" in captured.out
    assert "Result: AddCalculation: 20.0 Add 3.0 = 23.0" in captured.out
    assert "Calculation History:" in captured.out
    assert "1. PowerCalculation: 10.0 Power 5.0 = 100000.0" in captured.out
    assert "2. AddCalculation: 20.0 Add 3.0 = 23.0" in captured.out
def test_calculator_no_input(monkeypatch, capsys):
    """
    Test the calculator function's ability to handle the pressing enter with no command.
    AAA Pattern:
    - Arrange: Prepare the input 'help' followed by 'exit' to simulate user interactions.
    - Act: Call the calculator function.
    - Assert: Verify that the help message is displayed and the calculator exits gracefully.
    """
    # Arrange
    user_input = '\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Asserts
    captured = capsys.readouterr()
    assert "" in captured.out
    assert "Exiting calculator..." in captured.out

def test_calculator_invalid_input(monkeypatch, capsys):
    """
    Test the calculator function's handling of invalid input format.

    AAA Pattern:
    - Arrange: Prepare invalid input strings followed by 'exit'.
    - Act: Call the calculator function.
    - Assert: Verify that appropriate error messages are displayed.
    """
    # Arrange
    user_input = 'invalid input\nadd 5\nsubtract\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Invalid input. Please follow the format: <operation> <num1> <num2>. you can type help for more information on how to use this basic calulator" in captured.out
# Helper function to capture print statements
def run_calculator_with_input(monkeypatch, capsys, inputs):
    """
    Simulates user input and captures output from the calculator REPL.
    
    :param monkeypatch: pytest fixture to simulate user input
    :param inputs: list of inputs to simulate
    :return: captured output as a string
    """
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    return captured.out


def test_addition(monkeypatch,capsys):
    """Test addition operation in REPL."""
    inputs = ["add 2 3", "exit"]
    output = run_calculator_with_input(monkeypatch,capsys, inputs)
    assert "Result: 5.0" in output


def test_subtraction(monkeypatch, capsys):
    """Test subtraction operation in REPL."""
    inputs = ["subtract 5 2", "exit"]
    output = run_calculator_with_input(monkeypatch,capsys, inputs)
    assert "Result: 3.0" in output


def test_multiplication(monkeypatch, capsys):
    """Test multiplication operation in REPL."""
    inputs = ["multiply 4 5", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "Result: 20.0" in output

def test_power(monkeypatch, capsys):
    """Test power operation in REPL."""
    inputs = ["power 4 3", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "Result: 64.0" in output

def test_division(monkeypatch, capsys):
    """Test division operation in REPL."""
    inputs = ["divide 10 2", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "Result: 5.0" in output
def test_modulo(monkeypatch, capsys):
    """Test power operation in REPL."""
    inputs = ["modulo 4 3", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "Result: 1.0" in output


# Negative Tests
def test_invalid_operation(monkeypatch, capsys):
    """Test invalid operation in REPL."""
    inputs = ["bleh 5 3", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "Unsupported calculation type:" in output


def test_invalid_input_format(monkeypatch, capsys):
    """Test invalid input format in REPL."""
    inputs = ["add two three", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "Invalid input." in output


def test_division_by_zero(monkeypatch, capsys):
    """Test division by zero in REPL."""
    inputs = ["divide 5 0", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "Can't Divide By Zero" in output

def test_modulo_by_zero(monkeypatch, capsys):
    """Test modulo by zero in REPL."""
    inputs = ["modulo 5 0", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "Can't Divide By Zero" in output
def test_calculator_unexpected_exception(monkeypatch, capsys):
    """
    Test the calculator's handling of unexpected exceptions during calculation execution.

    AAA Pattern:
    - Arrange: Mock the execute method to raise an unexpected exception.
    - Act: Call the calculator function.
    - Assert: Verify that the appropriate error message is displayed.
    """
    # Arrange
    class MockCalculation:
        def execute(self):
            raise Exception("Mock exception during execution")
        def __str__(self):
            return "MockCalculation"

    def mock_create_calculation(operation, a, b):
        return MockCalculation()

    monkeypatch.setattr('app.calculation.CalculationFactory.create_calculation', mock_create_calculation)
    user_input = 'add 10 5\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "An error occurred during calculation: Mock exception during execution" in captured.out
    assert "Please try again." in captured.out

def test_calculator_eof_error(monkeypatch, capsys):
    """
    Test the calculator's handling of EOFError (Ctrl+D).

    AAA Pattern:
    - Arrange: Simulate an EOFError during input().
    - Act: Call the calculator function.
    - Assert: Verify that the calculator exits gracefully.
    """
    # Arrange
    def mock_input(prompt):
        raise EOFError()
    monkeypatch.setattr('builtins.input', mock_input)

    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "\nEOF detected. Exiting calculator. Goodbye!" in captured.out
    assert exc_info.value.code == 0
def test_calculator_keyboard_interrupt(monkeypatch, capsys):
    """
    Test the calculator's handling of KeyboardInterrupt (Ctrl+C).

    AAA Pattern:
    - Arrange: Simulate a KeyboardInterrupt during input().
    - Act: Call the calculator function.
    - Assert: Verify that the calculator exits gracefully.
    """
    # Arrange
    def mock_input(prompt):
        raise KeyboardInterrupt()
    monkeypatch.setattr('builtins.input', mock_input)

    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "\nKeyboard interrupt detected. Exiting calculator. Goodbye!" in captured.out
    assert exc_info.value.code == 0