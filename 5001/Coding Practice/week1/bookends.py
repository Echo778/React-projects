def main():        
    # input the number
    number = int(input("Enter number:"))

    # calculate the first and last number
    first_num = number // 1000
    last_num = number % 10

    # output the result
    print("The first number is", first_num)
    print("The last number is", last_num)


if __name__ == "__main__":
    main()
