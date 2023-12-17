"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
# Reformatted dictionary according to PEP 8 conventions
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")

while state_code != "":
    try:
        # Using EAFP approach
        print(f"{state_code.upper()} is {CODE_TO_NAME[state_code.upper()]}")
    except KeyError:
        print("Invalid short state")

    state_code = input("Enter short state: ")

# Loop that prints all the states and names neatly lined up with string formatting
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")
