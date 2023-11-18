name = input("Enter name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")

choice = ''

while choice.upper() != 'Q':

    choice = input(">>> ")

    if choice.upper() == 'H':
        print("Hello", name)
    elif choice.upper() == 'G':
        print("Goodbye", name)
    elif choice.upper() != 'Q':
        print("Invalid choice")

print("Finished.")
