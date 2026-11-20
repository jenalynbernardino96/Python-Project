# difficulty: hard
# gets three grades and calculates their average.

grade1 = float(input("Enter first grade: "))
grade2 = float(input("Enter second grade: "))
grade3 = float(input("Enter third grade: "))

average = (grade1 + grade2 + grade3) / 3

print(f"Average: {average:.2f}")

# expected output:
# Enter first grade: 96
# Enter second grade: 89
# Enter third grade: 99
# Average: 94.67
