def non_negatives():
    num = int(input("Enter an integer:"))
    while (num >= 0):
        print(num)
        num = int(input("Enter an integer:"))


def main():
    non_negatives()


if __name__ == "__main__":
    main()
