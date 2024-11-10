def read_wimbledon_data(filename):
    champions = {}
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as file:
        next(file)  # Skip header line
        for line in file:
            parts = line.strip().split(',')
            champion = parts[2]
            country = parts[1]

            champions[champion] = champions.get(champion, 0) + 1
            countries.add(country)

    return champions, countries

def main():
    filename = "wimbledon.csv"
    champions, countries = read_wimbledon_data(filename)

    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items(), key=lambda x: x[1], reverse=True):
        print(f"{champion} {wins}")

    print("\nThese countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

if __name__ == "__main__":
    main()
