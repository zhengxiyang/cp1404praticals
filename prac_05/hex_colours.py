# Constant dictionary of color names and their hexadecimal codes
COLOR_CODES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}


# Function to look up color code and handle invalid input
def get_color_code(color_name):
    try:
        return COLOR_CODES[color_name]
    except KeyError:
        return "Invalid color name"


# Program to allow user to look up hexadecimal color codes
while True:
    color_name = input("Enter color name (or blank to stop): ").strip()

    if not color_name:
        break

    color_code = get_color_code(color_name.capitalize())  # Case-insensitive matching
    print(f"{color_name}: {color_code}")
