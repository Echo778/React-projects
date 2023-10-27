def count_down(num):
    if num <= 0:
        print("please enter positive numbers")
    else:
        for i in range(num, 0, -1):
            print(i)


def main():
    count_down(4)


if __name__ == "__main__":
    main()
