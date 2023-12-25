import csv

filename = 'songs.csv'

songs = []

def load_songs(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            songs.append(row)

def display_menu():
    print("Menu:")
    print("L - List songs")
    print("A - Add new song")
    print("C - Complete a song")
    print("Q - Quit")

def handle_choice(choice):
    if choice == 'L':
        list_songs()
    elif choice == 'A':
        add_song()
    elif choice == 'C':
        complete_song()
    elif choice == 'Q':
        print("Thank you.")
    else:
        print("Invalid choice")

def main():
    print("Songs To Learn 1.0 - by Your Name")
    load_songs(filename)
    display_menu()
    choice = input(">>> ").upper()
    while choice != 'Q':
        handle_choice(choice)
        display_menu()
        choice = input(">>> ").upper()
    print("Goodbye!")


if __name__ == '__main__':
    main()
