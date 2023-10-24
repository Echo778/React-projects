def main():
    data1 = input("Enter data1: ")
    data2 = input("Enter data2: ")
    print(is_equal(data1, data2))


def is_equal(data1, data2):
    if data1 == data2:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
