Module 3: Statistics

Definition

- The "statistics" module is a built-in Python module used to perform statistical calculations.

- It is useful when analyzing numerical data, such as grades, survey results, and measurements.

How to Import

    import statistics

- After importing the module, we can use its functions to calculate statistical values.

Important Functions

- statistics.mean(data) - Calculates the arithmetic average.
- statistics.median(data) - Finds the middle value of the data.
- statistics.mode(data) - Finds the most frequently occurring value.
- statistics.stdev(data) - Calculates the sample standard deviation.
- statistics.variance(data) - Calculates the sample variance.

Code Examples

Example 1: Mean

    import statistics
    grades = [85, 90, 88, 92, 95]
    result = statistics.mean(grades)
    print("Mean:", result)

Explanation: The "mean()" function calculates the average of all the grades.

Sample Output:

    Mean: 90

Example 2: Median

    import statistics
    numbers = [10, 20, 30, 40, 50]
    result = statistics.median(numbers)
    print("Median:", result)

Explanation: The "median()" function finds the middle value after arranging the numbers in order.

Sample Output:

    Median: 30

Example 3: Mode

    import statistics
    numbers = [2, 4, 4, 6, 8, 4, 10]
    result = statistics.mode(numbers)
    print("Mode:", result)

Explanation: The "mode()" function finds the value that appears most frequently in the data.

Sample Output:

    Mode: 4

Advantages and Uses

- Helps analyze numerical information.
- Makes calculating averages easier.
- Identifies the middle value and most common value.
- Useful for school grades, surveys, and research data.

The Python "statistics" module makes statistical calculations easier. It helps programmers understand and analyze numerical data using built-in functions.
