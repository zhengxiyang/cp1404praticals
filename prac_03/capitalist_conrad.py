import random

# Constants
STARTING_PRICE = 10.00
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05
MIN_PRICE = 1.00
MAX_PRICE = 100.00
OUTPUT_FILE = "stock_prices.txt"

# Open the file for writing
out_file = open(OUTPUT_FILE, 'w')

# Initialize variables
price = STARTING_PRICE
day = 0

# Number of days to simulate
number_of_days = 425

# Simulate stock prices for the specified number of days
while MIN_PRICE < price < MAX_PRICE and day < number_of_days:
    price_change = 0

    # 50% chance of increase or decrease
    if random.randint(1, 2) == 1:  # decrease
        price_change = random.uniform(MAX_DECREASE, 0)
    else:  # increase
        price_change = random.uniform(0, MAX_INCREASE)

    price *= (1 + price_change)

    # Round to the nearest cent
    price = round(price, 2)

    # Print and write to the file
    print(f"On day {day + 1} price is: ${price:,.2f}")
    print(f"${price:,.2f}", file=out_file)

    day += 1

# Close the file
out_file.close()
