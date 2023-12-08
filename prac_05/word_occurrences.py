
"""
word_occurrences
Estimate: 30 minutes
Actual:   35 minutes
"""


def count_word_occurrences(text):
    word_counts = {}

    # Split the input text into words
    words = text.split()

    # Count occurrences of each word
    for word in words:
        word = word.lower()  # Make the counting case-insensitive
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def main():
    user_input = input("Enter a string: ")
    occurrences = count_word_occurrences(user_input)

    # Find the maximum width for formatting
    max_width = max(len(word) for word in occurrences)

    # Print the counts in sorted order
    for word, count in sorted(occurrences.items()):
        print(f"{word:{max_width}} : {count}")


if __name__ == "__main__":
    main()
