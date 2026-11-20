# difficulty: hard
#  collects and displays multiple student details.

name = input("Enter name: ")
age = int(input("Enter age: "))
section = input("Enter section: ")
grade = float(input("Enter general average: "))

print("\n--- STUDENT INFORMATION ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Section: {section}")
print(f"General Average: {grade:.2f}")

# expected output:
# Enter name: Jenalyn
# Enter age: 18
# Enter section: BSIT - 1B 
# Enter general average: 92

# --- STUDENT INFORMATION ---
# Name: Jenalyn
# Age: 18
# Section: BSIT - 1B
# General Average: 92.00
