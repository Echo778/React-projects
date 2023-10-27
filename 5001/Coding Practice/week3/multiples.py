def multiples():
    interger = int(input("Enter a non-zero integer: "))
    multiple = int(input("Enter multiple: "))
    while (multiple % interger != 0):
        multiple = int(input("Try again: "))


def main():
    multiples()


if __name__ == "__main__":
    main()
