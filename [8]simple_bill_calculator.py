# difficulty: hard
# calculates the total bill and the share per person.

bill = float(input("Enter the total bill: ₱"))
people = int(input("Enter the number of people: "))

if people > 0:
    share = bill / people
    print("\n--- BILL SUMMARY ---")
    print(f"Total Bill: ₱{bill:.2f}")
    print(f"Number of People: {people}")
    print(f"Each Person Pays: ₱{share:.2f}")
else:
    print("Invalid number of people!")

# expected output:
# Enter the total bill: ₱500
# Enter the number of people: 8

# --- BILL SUMMARY ---
# Total Bill: ₱500.00
# Number of People: 8
# Each Person Pays: ₱62.50
