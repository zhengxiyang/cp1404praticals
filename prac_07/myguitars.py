from guitar import Guitar

def main():
    """Program to read, store, and display guitars from a file."""
    guitars = []

    # Read guitars from file
    with open("guitars.csv", "r") as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))

    # Display all guitars
    print("These are the guitars we have read:")
    for guitar in guitars:
        print(guitar)

    # Sort the list of guitars by year and display
    guitars.sort()
    print("\nThese are the guitars sorted by year:")
    for guitar in guitars:
        print(guitar)

if __name__ == "__main__":
    main()
