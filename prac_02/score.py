"""Program to determine score result and print stars based on the score."""

import random


def main():
    """Main function to get score, print result, and generate random score."""
    score = float(input("Enter score: "))
    result = get_result(score)
    print(f"Your result: {result}")

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    print(f"Random score result: {get_result(random_score)}")


def get_result(score):
    """Determine the result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == '__main__':
    main()
