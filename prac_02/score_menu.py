import random
from score import get_score, calculate_result

def show_stars(score):
    print('*' * int(score))

def print_result(score):
    result = calculate_result(score)
    print(f"The result for the score {score} is: {result}")

def main_menu():
    print("\nMain Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def main():
    user_score = get_score()

    while True:
        main_menu()
        choice = input("Enter your choice: ").upper()

        if choice == 'G':
            user_score = get_score()
        elif choice == 'P':
            print_result(user_score)
        elif choice == 'S':
            show_stars(user_score)
        elif choice == 'Q':
            print("Farewell! Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter G, P, S, or Q.")

if __name__ == "__main__":
    main()