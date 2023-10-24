def main():
    data1 = input("Enter data1: ")
    data2 = input("Enter data2: ")
    print(first(data1, data2))


def first(data1, data2):
    try:
        data1 = int(data1)
        data2 = int(data2)
        return min(data1, data2)
    except ValueError:
        if isinstance(data1, str) and isinstance(data2, str):
            return min(data1, data2)


if __name__ == "__main__":
    main()
