# File: lists_warmup.py

numbers = [3, 1, 4, 1, 5, 9, 2]

# Values for the given expressions
# Uncomment and run each line to check your answers

# print(numbers[0])       # Expected output: 3
# print(numbers[-1])      # Expected output: 2
# print(numbers[3])       # Expected output: 1
# print(numbers[:-1])     # Expected output: [3, 1, 4, 1, 5, 9]
# print(numbers[3:4])      # Expected output: [1]
# print(5 in numbers)     # Expected output: True
# print(7 in numbers)     # Expected output: False
# print("3" in numbers)   # Expected output: False
# print(numbers + [6, 5, 3])  # Expected output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change the first element of numbers to "ten"
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all elements from numbers except the first two (slice)
# print(numbers[2:])      # Expected output: [4, 1, 5, 9, 1]

# Print whether 9 is an element of numbers
# print(9 in numbers)     # Expected output: True
