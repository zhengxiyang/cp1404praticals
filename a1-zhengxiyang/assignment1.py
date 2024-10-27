"""
CP1404 Assignment 1 - Travel Tracker
Name:Yang zhengxi
Date started:2024/10/26
GitHub URL:https://github.com/cp1404-students/a1-zhengxiyang.git
"""
import random

VISITED = 'v'
UNVISITED = 'n'


def load_places(filename):
    places = []
    with open(filename, 'r') as file:
        for line in file:
            name, country, priority, visited = line.strip().split(',')
            places.append([name, country, int(priority), visited])
    return places


def display_places(places):
    unvisited_count = sum(1 for place in places if place[3] == UNVISITED)
    print()
    for index, place in enumerate(sorted(places, key=lambda x: (x[3], x[2]))):
        status = '*' if place[3] == UNVISITED else ''
        print(f"{status}{index + 1}. {place[0]} in {place[1]} {place[2]}")
    print(f"{len(places)} places tracked. You still want to visit {unvisited_count} places.")


def recommend_place(places):
    unvisited_places = [place for place in places if place[3] == UNVISITED]
    if not unvisited_places:
        print("No places left to visit!")
    else:
        place = random.choice(unvisited_places)
        print(f"Not sure where to visit next?\nHow about... {place[0]} in {place[1]}?")


def add_place(places):
    name = input("Name:\n")
    while not name.strip():
        print("Input can not be blank")
        name = input("Name:\n")

    country = input("Country:\n")
    while not country.strip():
        print("Input can not be blank")
        country = input("Country:\n")

    priority = input("Priority:\n")
    while not priority.isdigit() or int(priority) <= 0:
        print("Invalid input; enter a valid number")
        priority = input("Priority:\n")

    places.append([name, country, int(priority), UNVISITED])
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")


def mark_visited(places):
    unvisited_places = [place for place in places if place[3] == UNVISITED]
    if not unvisited_places:
        print("No unvisited places")
        return

    display_places(places)
    choice = input("Enter the number of a place to mark as visited\n")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(places):
        if not choice.isdigit():
            print("Invalid input; enter a valid number")
        else:
            print("Invalid place number")
        choice = input("Enter the number of a place to mark as visited\n")

    index = int(choice) - 1
    if places[index][3] == VISITED:
        print(f"You have already visited {places[index][0]}")
    else:
        places[index][3] = VISITED
        print(f"{places[index][0]} in {places[index][1]} visited!")


def save_places(filename, places):
    with open(filename, 'w') as file:
        for place in places:
            file.write(','.join(map(str, place)) + '\n')


def main():
    filename = 'places.csv'
    places = load_places(filename)
    print(f"{len(places)} places loaded from {filename}")

    while True:
        print("\nMenu:")
        print("D - Display all places")
        print("R - Recommend a random place")
        print("A - Add a new place")
        print("M - Mark a place as visited")
        print("Q - Quit")

        choice = input(">>> ").strip().lower()
        if choice == 'd':
            display_places(places)
        elif choice == 'r':
            recommend_place(places)
        elif choice == 'a':
            add_place(places)
        elif choice == 'm':
            mark_visited(places)
        elif choice == 'q':
            save_places(filename, places)
            print(f"{len(places)} places saved to {filename}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


if __name__ == "__main__":
    main()

