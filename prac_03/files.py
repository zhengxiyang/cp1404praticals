# Task 1: Write the user's name to "name.txt"
user_name = input("Enter your name: ")
with open("name.txt", 'w') as name_file:
    name_file.write(user_name)

# Task 2: Read the name from "name.txt" and print it
with open("name.txt", 'r') as name_file:
    stored_name = name_file.read()
    print(f"Your name is {stored_name}")

# Task 3: Read the first two numbers from "numbers.txt" and print their sum
with open("numbers.txt", 'r') as numbers_file:
    number1 = int(numbers_file.readline().strip())
    number2 = int(numbers_file.readline().strip())
    total = number1 + number2
    print(f"The sum of the first two numbers is: {total}")

# Task 4: Read all numbers from "numbers.txt" and print their total
total_all_numbers = 0
with open("numbers.txt", 'r') as numbers_file:
    for line in numbers_file:
        total_all_numbers += int(line.strip())

print(f"The total of all numbers is: {total_all_numbers}")
