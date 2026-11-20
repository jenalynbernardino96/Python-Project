Module 2: Math

Definition

- The "math" module is a built-in Python module that provides mathematical functions and constants.

- It is useful for performing calculations involving square roots, powers, factorials, rounding, and other mathematical operations.

How to Import

    import math

- After importing the module, we can access its functions using "math.function_name()".

Important Functions and Constants

- math.sqrt(x) - Calculates the square root of a number.
- math.factorial(x) - Calculates the factorial of a non-negative integer.
- math.pow(x, y) - Raises x to the power of y and returns a float.
- math.pi - Represents the mathematical constant pi.
- math.ceil(x) - Rounds a number upward to the nearest integer.
- math.floor(x) - Rounds a number downward to the nearest integer.

Code Examples

Example 1: Square Root

    import math
    number = 64
    result = math.sqrt(number)
    print("Square root:", result)

Explanation: The "sqrt()" function calculates the square root of 64.

Sample Output:

    Square root: 8.0

Example 2: Factorial

    import math
    number = 5
    result = math.factorial(number)
    print("Factorial:", result)

Explanation: The "factorial()" function calculates the product of all positive integers from 1 up to the given number.

For example, 5! = 5 × 4 × 3 × 2 × 1.

Sample Output:

    Factorial: 120

Example 3: Circle Area

    import math
    radius = 7
    area = math.pi * math.pow(radius, 2)
    print("Circle area:", area)

Explanation: This program calculates the area of a circle using the formula:

Area = π × radius²

The "math.pi" constant provides the value of pi, while "math.pow()" calculates the radius squared.

Sample Output:

    Circle area: 153.93804002589985

Advantages and Uses

- Makes mathematical calculations easier.
- Provides ready-made mathematical functions.
- Reduces the need to write complicated formulas manually.
- Useful for scientific, educational, and engineering programs.

The Python "math" module provides useful mathematical functions and constants. It helps programmers perform accurate and efficient mathematical calculations.