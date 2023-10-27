def count_up(num):
    if num < 0:
        print("please enter positive numbers")
    else:
        for i in range(1, num + 1):
            print(i)


def main():
    count_up(4)


if __name__ == "__main__":
    main()
