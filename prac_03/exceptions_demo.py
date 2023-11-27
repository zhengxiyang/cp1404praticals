# File: exceptions_demo.py

"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user enters something that is not a valid integer
when prompted for the numerator or denominator.

2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if the user enters 0 as the denominator because division by zero is undefined.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
I changed the code to check if the denominator is zero before performing the division.
If the denominator is zero, it raises a ZeroDivisionError with a custom error message.
This avoids the possibility of a ZeroDivisionError and provides a more informative error message to the user.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check if the denominator is zero before performing the division
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero!")

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError as e:
    print(e)

print("Finished.")
