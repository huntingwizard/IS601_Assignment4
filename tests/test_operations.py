import pytest
from typing import Union   
from app.operations import Operations 


Number = Union[int, float]
@pytest.mark.parametrize(
        "a, b, expected",
        [
            (1,1,2),
            (1,-11,-10),
            (0,0,0),
            (-1,-11,-12),
            (3.5, 3.5, 7.0),
            (-2.5, 4.5, 2.0),

        ],
        ids=[
        "add_two_positive_integers",
        "add_negative_and_positive_integer",
        "add_two_zeros",
        "add_two_negative_integers",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float",
        ]
)

def test_addition(a: Number, b: Number, expected: Number):
    """
    Test the 'addition' method of the Operations class with various input combinations.

    This parameterized test verifies that the 'addition' method correctly adds two numbers,
    whether they are positive, negative, integers, or floats. By using parameterization,
    we can efficiently test multiple scenarios without redundant code.
    Parameters:
    - a (Number): The first number to add.
    - b (Number): The second number to add.
    - expected (Number): The expected result of the addition.
    Steps:
    1. Call the 'addition' method with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.
    """
    result = Operations.addition(a, b)
    
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
        "a, b, expected",
        [
            (2,1,1),
            (-10,-11,1),
            (0,0,0),
            (-12,-11,-1),
            (7.0, 3.5, 3.5),
            (2.0, 4.5, -2.5),

        ],
        ids=[
        "subtract_two_positive_integers",
        "subtract_negative_and_positive_integer",
        "subtract_two_zeros",
        "subtract_two_negative_integers",
        "subtract_two_positive_floats",
        "subtract_negative_float_and_positive_float",
        ]
)
def test_subtraction(a: Number, b: Number, expected: Number):
    """
    Test the 'subtraction' method of the Operations class with various input combinations.
    This parameterized test verifies that the 'subtraction' method correctly subtracts the
    second number from the first, handling both positive and negative values, as well as
    integers and floats. Parameterization allows for comprehensive testing of multiple cases.
    Parameters:
    - a (Number): The number to subtract from.
    - b (Number): The number to subtract.
    - expected (Number): The expected result of the subtraction.
    Steps:
    1. Call the 'subtraction' method with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    """

    result = Operations.subtraction(a, b)
        
    assert result == expected, f"Expected subtraction({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (42, 3, 126),     
        (1230, 0, 0),      
        (-5, -3, 15),       
        (3.5, 4.0, 14.0),  
        (-3.5, 4.0, -14.0),
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_zero_with_positive_integer",
        "multiply_two_negative_integers",
        "multiply_two_positive_floats",
        "multiply_negative_float_with_positive_float",
    ]
)
def test_multiplication(a: Number, b: Number, expected: Number):
    """
    Test the 'multiplication' method of the Operations class with various input combinations.
    This parameterized test verifies that the 'multiplication' method correctly multiplies two numbers,
    handling both positive and negative values, as well as integers and floats. Parameterization
    enables efficient testing of multiple scenarios in a concise manner.
    Parameters:
    - a (Number): The first number to multiply.
    - b (Number): The second number to multiply.
    - expected (Number): The expected result of the multiplication.
    Steps:
    1. Call the 'multiplication' method with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    """
    result = Operations.multiplication(a, b)
        
    assert result == expected, f"Expected multiplication({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 8),     
        (1230, 0, 1),      
        (-5, -3, -0.008),       
        (1.5, 2.0, 2.25),  
        (-1.5, 3.0, -3.375),
    ],
    ids=[
        "power_two_positive_integers",
        "power_zero_with_positive_integer",
        "power_two_negative_integers",
        "power_two_positive_floats",
        "power_negative_float_with_positive_float",
    ]
)
def test_power(a: Number, b: Number, expected: Number):
    """
    Test the 'power' method of the Operations class with various input combinations.
    This parameterized test verifies that the 'power' method correctly multiplies two numbers,
    handling both positive and negative values, as well as integers and floats. Parameterization
    enables efficient testing of multiple scenarios in a concise manner.
    Parameters:
    - a (Number): The first number to power.
    - b (Number): The second number to power.
    - expected (Number): The expected result of the power.
    Steps:
    1. Call the 'multiplication' method with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    """
    result = Operations.power(a, b)
        
    assert result == expected, f"Expected power({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (126, 3, 42),        
        (0, 1230, 0),        
        (-15, -3, 5),        
        (14.0, 4.0, 3.5), 
        (-14.0, 4.0, -3.5), 
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_positive_integer_with_zero",
        "divide_two_negative_integers",
        "divide_two_positive_floats",
        "divide_negative_float_with_positive_float",
    ]
)

def test_division(a: Number, b: Number, expected: Number):
    """
    Test the 'division' method of the Operations class with various input combinations.
    This parameterized test verifies that the 'division' method correctly divides the first
    number by the second, handling both positive and negative values, as well as integers
    and floats. Parameterization allows for efficient and comprehensive testing across multiple cases.
    Parameters:
    - a (Number): The dividend.
    - b (Number): The divisor.
    - expected (float): The expected result of the division.
    Steps:
    1. Call the 'division' method with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    """
    result = Operations.division(a, b)
            
    assert result == expected, f"Expected division({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (127, 3, 1),        
        (0, 1230, 0),        
        (-16, -3, -1),        
        (14.0, 4.0, 2.0), 
        (-14.0, 4.0, 2.0), 
    ],
    ids=[
        "modulo_two_positive_integers",
        "modulo_positive_integer_with_zero",
        "modulo_two_negative_integers",
        "modulo_two_positive_floats",
        "modulo_negative_float_with_positive_float",
    ]
)

def test_modulo(a: Number, b: Number, expected: Number):
    """
    Test the 'modulo' method of the Operations class with various input combinations.
    This parameterized test verifies that the 'modulo' method correctly divides the first
    number by the second, handling both positive and negative values, as well as integers
    and floats. Parameterization allows for efficient and comprehensive testing across multiple cases.
    Parameters:
    - a (Number): The dividend.
    - b (Number): The divisor.
    - expected (float): The expected result of the modulus.
    Steps:
    1. Call the 'modulo' method with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    """
    result = Operations.modulo(a, b)
            
    assert result == expected, f"Expected modulo({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b",
    [
        (23, 0),   
        (-53253, 0), 
        (0, 0),    
    ],
    ids=[
        "divide_positive_dividend_by_zero",
        "divide_negative_dividend_by_zero",
        "divide_zero_by_zero",
    ]
)
def test_division_DivideByZero(a: Number, b: Number):
    with pytest.raises(ValueError, match="Can't Divide By Zero") as excinfo:
        Operations.division(a, b)
    
    assert "Can't Divide By Zero" in str(excinfo.value), \
        f"Expected error message 'Can't Divide By Zero', but got '{excinfo.value}'"

@pytest.mark.parametrize(
    "a, b",
    [
        (23, 0),   
        (-53253, 0), 
        (0, 0),    
    ],
    ids=[
        "modulo_positive_dividend_by_zero",
        "modulo_negative_dividend_by_zero",
        "modulo_zero_by_zero",
    ]
)
def test_division_ModuloByZero(a: Number, b: Number):
    with pytest.raises(ValueError, match="Can't Divide By Zero") as excinfo:
        Operations.modulo(a, b)
    
    assert "Can't Divide By Zero" in str(excinfo.value), \
        f"Expected error message 'Can't Divide By Zero', but got '{excinfo.value}'"