
"""
emails
Estimate: 20 minutes
Actual:   27 minutes
"""

def extract_name(email):
    """
    Extracts a name from the given email using the part before the '@' symbol.
    Converts the name to title case.
    """
    return email.split('@')[0].title()

def main():
    user_data = {}

    while True:
        email = input("Email: ").strip()

        if not email:
            break

        name = extract_name(email)

        # Confirm the extracted name with the user
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation in {'', 'y'}:
            user_data[email] = name
        else:
            # If the user does not press Enter or Y, ask for their name
            user_name = input("Name: ").strip().title()
            user_data[email] = user_name

    # Print the stored emails and names
    for email, name in user_data.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
