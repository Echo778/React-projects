def main():
    str_val = input("Enter string value: ")
    int_val1 = int(input("Enter first integer value: "))
    int_val2 = int(input("Enter second integer value: "))
    int_val3 = int(input("Enter third integer value: "))
    print(build_string(str_val, int_val1, int_val2, int_val3))


def build_string(str_val, int_val1, int_val2, int_val3):
    line1 = str_val * int_val1
    line2 = str_val * int_val2
    line3 = str_val * int_val3
    return f"{line1}\n{line2}\n{line3}"


if __name__ == "__main__":
    main()
