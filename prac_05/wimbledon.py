
"""
wimbledon

Estimate: 60 minutes
Actual:   85 minutes
"""

import csv

def read_csv(filename):
    """
    Read the CSV file and return a list of lists containing the data.
    """
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        csv_reader = csv.reader(in_file)
        data = [row for row in csv_reader]

    return data

def get_champions_and_wins(data):
    """
    Process the data to get the champions and the number of times they have won.
    Returns a dictionary with champions as keys and their win counts as values.
    """
    champions_dict = {}

    for row in data:
        champion_name = row[1]
        champions_dict[champion_name] = champions_dict.get(champion_name, 0) + 1

    return champions_dict

def get_countries(data):
    """
    Process the data to get the countries of the champions in alphabetical order.
    Returns a set of unique country codes.
    """
    countries_set = set()

    for row in data:
        country_code = row[2]
        countries_set.add(country_code)

    return countries_set

def main():
    filename = "wimbledon.csv"
    data = read_csv(filename)

    champions_and_wins = get_champions_and_wins(data)
    print("\nWimbledon Champions:")
    for champion, wins in sorted(champions_and_wins.items()):
        print(f"{champion} {wins}")

    countries = get_countries(data)
    print("\nThese countries have won Wimbledon:")
    countries_string = ", ".join(sorted(countries))
    print(countries_string)

if __name__ == "__main__":
    main()
