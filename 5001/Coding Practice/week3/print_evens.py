def print_evens():
    nums = 101
    for num in range(2, nums):
        if num % 2 == 0:
            print(num)


def main():
    print_evens()


if __name__ == "__main__":
    main()
