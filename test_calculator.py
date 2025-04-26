import pytest
from calculator import Calculator

# Normal testing

# def test_add():
#     calc = Calculator()
#     assert calc.add(3, 5) == 8
#     assert calc.add(-1, 1) == 0
#     assert calc.add(-1, -1) == -2

# def test_subtract():
#     calc = Calculator()
#     assert calc.subtract(5, 3) == 2
#     assert calc.subtract(1, 5) == -4
#     assert calc.subtract(-5, -3) == -2

# def test_multiply():
#     calc = Calculator()
#     assert calc.multiply(3, 5) == 15
#     assert calc.multiply(-2, 4) == -8
#     assert calc.multiply(-3, -3) == 9

#     assert calc.multiply(2.5, 4.0) == 10.0  #float
#     assert calc.multiply(-1.5, 2.0) == -3.0
#     assert calc.multiply(3.3, 0.0) == 0.0

# def test_divide():
#     calc = Calculator()

#     assert calc.divide(10, 2) == 5
#     assert calc.divide(9, 3) == 3

#     assert calc.divide(5, 2) == 2.5   #decimal
#     assert calc.divide(7.5, 2.5) == 3.0

#     with pytest.raises(ValueError, match="Cannot divide by zero"):
#         calc.divide(5, 0)


#----------------------------------------------------------------------------------------------------------------------------
# Parameterized test

# @pytest.mark.parametrize("a, b, expected", [
#     (3, 5, 8),
#     (-1, 1, 0),
#     (-1, -1, -2),
#     (0, 0, 0)
# ])

# def test_add_parameterized(a, b, expected):
#     calc = Calculator()
#     assert calc.add(a, b) == expected


# @pytest.mark.parametrize("a, b, expected", [
#     (5, 3, 2),
#     (1, 5, -4),
#     (-5, -3, -2),
#     (0, 0, 0)
# ])
# def test_subtract(a, b, expected):
#     calc = Calculator()
#     assert calc.subtract(a, b) == expected


# @pytest.mark.parametrize("a, b, expected", [
#     (3, 5, 15),
#     (-2, 4, -8),
#     (-3, -3, 9),
#     (2.5, 4.0, 10.0),
#     (-1.5, 2.0, -3.0),
#     (3.3, 0.0, 0.0)
# ])
# def test_multiply(a, b, expected):
#     calc = Calculator()
#     assert calc.multiply(a, b) == expected


# @pytest.mark.parametrize("a, b, expected", [
#     (10, 2, 5),
#     (9, 3, 3),
#     (5, 2, 2.5),
#     (7.5, 2.5, 3.0)
# ])
# def test_divide(a, b, expected):
#     calc = Calculator()
#     assert calc.divide(a, b) == expected

# def test_divide_by_zero(calculator):
#     with pytest.raises(ValueError, match="Cannot divide by zero"):
#         calculator.divide(5, 0)


# @pytest.mark.parametrize("base, exponent, expected", [
#     (2, 3, 8),
#     (5, 0, 1),
#     (0, 5, 0),
#     (2, -1, 0.5),
#     (-2, 2, 4),
#     (4, 0.5, 2.0)  # square root
# ])
# def test_power(base, exponent, expected):
#     calc = Calculator()
#     assert calc.power(base, exponent) == expected


#-----------------------------------------------------------------------------------------------------------------------
# Test by Conftest file 

# @pytest.mark.parametrize("a, b, expected", [
#     (3, 5, 8),
#     (-1, 1, 0),
#     (-1, -1, -2),
#     (0, 0, 0)
# ])
# def test_add(calculator, a, b, expected):
#     assert calculator.add(a, b) == expected



# @pytest.mark.parametrize("a, b, expected", [
#     (5, 3, 2),
#     (1, 5, -4),
#     (-5, -3, -2),
#     (0, 0, 0)
# ])
# def test_subtract(calculator, a, b, expected):
#     assert calculator.subtract(a, b) == expected



# @pytest.mark.parametrize("a, b, expected", [
#     (3, 5, 15),
#     (-2, 4, -8),
#     (-3, -3, 9),
#     (2.5, 4.0, 10.0),
#     (-1.5, 2.0, -3.0),
#     (3.3, 0.0, 0.0)
# ])
# def test_multiply(calculator, a, b, expected):
#     assert calculator.multiply(a, b) == expected



# @pytest.mark.parametrize("a, b, expected", [
#     (10, 2, 5),
#     (9, 3, 3),
#     (5, 2, 2.5),
#     (7.5, 2.5, 3.0)
# ])
# def test_divide(calculator, a, b, expected):
#     assert calculator.divide(a, b) == expected

# def test_divide_by_zero(calculator):
#     with pytest.raises(ValueError, match="Cannot divide by zero"):
#         calculator.divide(5, 0)


# @pytest.mark.parametrize("base, exponent, expected", [
#     (2, 3, 8),
#     (5, 0, 1),
#     (0, 5, 0),
#     (2, -1, 0.5),
#     (-2, 2, 4),
#     (4, 0.5, 2.0)
# ])
# def test_power(calculator, base, exponent, expected):
#     assert calculator.power(base, exponent) == expected

# -------------------------------------------------------------------------------------------------------
# New functions
 
# @pytest.mark.parametrize("n, expected", [
#     (0, 1),
#     (1, 1),
#     (5, 120),
#     (7, 5040)
# ])
# def test_factorial(calculator, n, expected):
#     assert calculator.factorial(n) == expected

# @pytest.mark.parametrize("n", [-1, -5, -10])
# def test_factorial_negative(calculator, n):
#     with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
#         calculator.factorial(n)


# @pytest.mark.parametrize("n, expected", [
#     (0, 0),
#     (1, 1),
#     (5, 5),
#     (7, 13)
# ])
# def test_fibonacci(calculator, n, expected):
#     assert calculator.fibonacci(n) == expected

# @pytest.mark.parametrize("n", [-1, -3, -8])
# def test_fibonacci_negative(calculator, n):
#     with pytest.raises(ValueError, match="Fibonacci is not defined for negative numbers"):
#         calculator.fibonacci(n)


#-----------------------------------------------------------------------------------------------------------------
# Precision Calculator Testing  

def test_addition(precise_calculator):
    assert precise_calculator.add(1.2345, 2.3456) == 3.58

def test_subtraction(precise_calculator):
    assert precise_calculator.subtract(5.55, 2.22) == 3.33


# With Parameterized 

@pytest.mark.parametrize("a, b", [
    (1.1111, 2.2222),
    (5.5555, 4.4444),
])
def test_custom_precision_addition(precise_calculator, a, b):
    precision = precise_calculator.precision
    expected = round(a + b, precision)
    assert precise_calculator.add(a, b) == expected




