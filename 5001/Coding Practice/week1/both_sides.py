def main():   
    # input the value
    value = int(input("Enter value: "))

    # check the value is even or odd, negative or positive.
    if value % 2 == 0:  # check if the value is even
        if value < 0:   # value is negative
            print("even negative number")
        else:   # value is positive
            print("even positive number")

    else:  # if the value is odd
        if value < 0:   # value is negative
            print("odd negative number")
        else:   # value is positive
            print("odd positive number")


if __name__ == "__main__":
    main()
