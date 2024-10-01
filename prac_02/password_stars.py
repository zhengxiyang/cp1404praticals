"""Program that checks the password length and prints asterisks."""

MIN_PASSWORD_LENGTH = 8

def main():
    """Main function to get password and print asterisks."""
    password = get_password(MIN_PASSWORD_LENGTH)
    print_asterisks(password)


def get_password(min_length):
    """Get a password of at least the required length."""
    password = input(f"Enter a password of at least {min_length} characters: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input(f"Enter a password of at least {min_length} characters: ")
    return password


def print_asterisks(password):
    """Print asterisks for each character in the password."""
    print('*' * len(password))


if __name__ == '__main__':
    main()
