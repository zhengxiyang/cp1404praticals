import random

def get_score():
    try:
        score = float(input("Enter score: "))
        return score
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return None

def calculate_result(score):
    if 90 > score >= 50:
        return "Passable"
    elif 100 >= score >= 90:
        return "Excellent"
    elif 0 <= score < 50:
        return "Bad"
    else:
        return "Invalid score"

def main():
    user_score = get_score()

    if user_score is not None:
        user_result = calculate_result(user_score)
        print(f"User's score result: {user_result}")

        random_score = random.uniform(0, 100)
        print(f"Random score: {random_score}")

        random_result = calculate_result(random_score)
        print(f"Random score result: {random_result}")

if __name__ == "__main__":
    main()
