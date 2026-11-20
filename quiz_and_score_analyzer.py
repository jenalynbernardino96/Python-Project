
import random
import math
import statistics

round_scores = []


def play_quiz():
    score = 0
    total_questions = 5

    print("\n---- MATH QUIZ ----")
    print("Answer the 5 randomly generated questions!")

    for question_number in range(1, total_questions + 1):
        operation = random.choice([
            "addition",
            "multiplication",
            "square root",
            "factorial",
            "power"
        ])

        print(f"\nQuestion {question_number}:")

        if operation == "addition":
            num1 = random.randint(1, 50)
            num2 = random.randint(1, 50)
            answer = num1 + num2
            print(f"What is {num1} + {num2}?")

        elif operation == "multiplication":
            num1 = random.randint(1, 12)
            num2 = random.randint(1, 12)
            answer = num1 * num2
            print(f"What is {num1} x {num2}?")

        elif operation == "square root":
            num = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
            answer = int(math.sqrt(num))
            print(f"What is the square root of {num}?")

        elif operation == "factorial":
            num = random.randint(1, 6)
            answer = math.factorial(num)
            print(f"What is the factorial of {num}?")

        else:
            num1 = random.randint(2, 5)
            num2 = random.randint(2, 3)
            answer = int(math.pow(num1, num2))
            print(f"What is {num1} raised to the power of {num2}?")

        try:
            user_answer = int(input("Your answer: "))

            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer is {answer}.")

        except ValueError:
            print(f"Invalid input! The correct answer is {answer}.")

    percentage = (score / total_questions) * 100
    round_scores.append(score)

    print("\n---- QUIZ RESULT ----")
    print(f"Correct answers: {score}/{total_questions}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage == 100:
        print("Excellent work!")
    elif percentage >= 60:
        print("Good job!")
    else:
        print("Keep practicing!")


def show_statistics():
    print("\n---- SCORE ANALYZER ----")

    if not round_scores:
        print("No quiz scores available yet.")
        print("Play at least one round first.")
        return

    print("Scores per round:", round_scores)
    print("Total rounds played:", len(round_scores))
    print(f"Average score: {statistics.mean(round_scores):.2f}")
    print(f"Median score: {statistics.median(round_scores)}")
    print("Highest score:", max(round_scores))
    print("Lowest score:", min(round_scores))

    modes = statistics.multimode(round_scores)
    print("Most common score(s):", modes)


def main():
    while True:
        print("MATH QUIZ AND SCORE ANALYZER")
        print("1. Play Math Quiz")
        print("2. View Score Statistics")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            play_quiz()

        elif choice == "2":
            show_statistics()

        elif choice == "3":
            print("\nThank you for playing!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


main()