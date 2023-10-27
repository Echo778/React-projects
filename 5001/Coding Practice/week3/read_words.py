def read_words():
    words = []
    word = input("Enter a word:")
    while (word != "stop"):
        words.append(word)
        word = input("Enter a word:")
    result = " ".join(words)
    print(result)


def main():
    read_words()


if __name__ == "__main__":
    main()
