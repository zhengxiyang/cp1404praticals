HEX_COLOURS = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Beige": "#f5f5dc",
    "Black": "#000000",
    "Blue": "#0000ff",
    "Chartreuse": "#7fff00",
    "Coral": "#ff7f50",
    "Crimson": "#dc143c",
    "DarkGreen": "#006400"
}

def main():
    while True:
        colour_name = input("Enter a colour name (or press Enter to quit): ").strip()
        if not colour_name:
            break
        colour_code = HEX_COLOURS.get(colour_name.capitalize())
        if colour_code:
            print(f"The code for {colour_name} is {colour_code}")
        else:
            print("Invalid colour name")

if __name__ == "__main__":
    main()