def main():   
    # input the value
    number = float(input("Enter value: "))

    # clamp the number to be between 1 and 100
    clamped_number = max(1, min(number, 100))

    # check if clamping was required
    if clamped_number != number:
        if clamped_number == 1:
            print("Too small, clamping required")
        else:
            print("Too big, clamping required")

    # output the clamped number
    print("Value is", clamped_number)


if __name__ == "__main__":
    main()
