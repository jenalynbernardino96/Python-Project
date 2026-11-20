Module 1: Random

Definition

- The "random" module is a built-in Python module used to generate pseudo-random numbers and make random selections.

- It is useful when creating games, quizzes, simulations, and programs that require random results.

How to Import

    import random

- The "import" statement allows us to use the functions provided by the random module.

Important Functions

- random.randint(a, b) - Generates a random integer between a and b, inclusive.
- random.choice(sequence) - Selects one random item from a sequence.
- random.shuffle(list) - Randomly rearranges the items in a list.
- random.random() - Generates a random decimal from 0.0 up to, but not including, 1.0.
- random.uniform(a, b) - Generates a random floating-point number between a and b.

Code Examples

Example 1: Random Integer

    import random
    number = random.randint(1, 100)
    print("Random number:", number)

Explanation: The "randint()" function generates a random whole number from 1 to 100.

Sample Output:

    Random number: 60

Example 2: Random Choice

    import random
    fruits = ["Apple", "Banana", "Mango", "Orange"]
    chosen_fruit = random.choice(fruits)
    print("Chosen fruit:", chosen_fruit)

Explanation: The "choice()" function selects one random item from the fruits list.

Sample Output:

    Chosen fruit: Mango

Example 3: Random Shuffle

    import random
    students = ["Alexis", "James", "Tyler", "Sammy"]
    random.shuffle(students)
    print("Random student order:", students)

Explanation: The "shuffle()" function changes the order of items in the list randomly.

Sample Output:

    Random student order: ['Tyler', 'Sammy', 'Alexis', 'James']

Advantages and Uses

- Useful for creating games and quizzes.
- Helps generate random numbers.
- Can randomly select items from a list.
- Can shuffle items into a different order.

The Python "random" module makes it easy to generate random values and selections. It is useful in different applications that require unpredictable results.
