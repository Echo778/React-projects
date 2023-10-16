def main():   
    # input 4 nums
    num1 = int(input("please enter the first number:"))
    num2 = int(input("please enter the second number:"))
    num3 = int(input("please enter the third number:"))
    num4 = int(input("please enter the fourth number:"))

    # check if there are two pairs and output the result
    # it has three situations if there are two pairs
    if (num1 == num2 and num3 == num4) or \
       (num1 == num3 and num2 == num4) or \
       (num1 == num4 and num2 == num3):
        print("two pairs")
    else:
        print("not two pairs")


if __name__ == "__main__":
    main()
