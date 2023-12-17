from guitar import Guitar

def main():
    guitars = []

    with open('guitars.csv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))

    guitars.sort(key=lambda guitar: guitar.year)

    print("These are my guitars:")
    for guitar in guitars:
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"{guitar.name} ({guitar.year}), worth ${guitar.cost:,.2f} {vintage_string}")

main()
