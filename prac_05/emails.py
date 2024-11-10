def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = ' '.join(parts).title()
    return name

def main():
    email_to_name = {}
    while True:
        email = input("Email: ").strip()
        if not email:
            break
        name = get_name_from_email(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm != 'y' and confirm != '':
            name = input("Name: ").strip().title()
        email_to_name[email] = name

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
