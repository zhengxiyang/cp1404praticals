try:
    items = int(input("Number of items: "))

    total_price = 0

    for i in range(items):
        item_price = float(input("Price of item {}: ".format(i + 1)))
        total_price += item_price

    if total_price > 100:
        discount = 0.1 * total_price
        total_price -= discount


    print("Total price for {} items is ${:.2f}".format(items, total_price))

except ValueError:
    print("Invalid input. Please enter valid numbers.")
