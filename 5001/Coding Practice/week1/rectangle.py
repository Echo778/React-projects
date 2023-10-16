def main():    
    # input the height and the width of the rectangle
    width = float(input("Enter width:"))
    height = float(input("Enter height:"))

    # calculate the area of the rectangle
    area = height * width

    # calculate the perimeter of the rectangle
    perimeter = 2 * (height + width)

    # calculate the length of the diagonal 
    length_diagonal = (height ** 2 + width ** 2) ** 0.5

    # output the result
    print("The area of the rectangle is", area)
    print("The perimeter of the rectangle is", perimeter)
    print("The diagonal of the rectangle is", length_diagonal)


if __name__ == "__main__":
    main()
