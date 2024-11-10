def main():
    text = input("Text: ").strip()
    words = text.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    max_word_length = max(len(word) for word in word_count)
    for word in sorted(word_count):
        print(f"{word:{max_word_length}} : {word_count[word]}")

if __name__ == "__main__":
    main()
