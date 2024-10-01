def main():
    """Main function to handle score menu options."""
    MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Result: {get_result(score)}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell!")


def get_valid_score():
    """Get a valid score from the user between 0 and 100."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score: "))
    return score


def get_result(score):
    """Determine the result based on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print stars as many as the score."""
    print('*' * int(score))


if __name__ == '__main__':
    main()
