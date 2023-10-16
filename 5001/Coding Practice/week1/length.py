def main():    
    # input the information in meters
    meters = float(input("Enter length:"))

    # convert meters to inches, feet, and miles
    inches = meters * 39.3701
    feet = meters * 3.2808416666666666
    miles = meters * 0.000621371

    # output the results
    print("The length in inches is", inches)
    print("The length in feet is", feet)
    print("The length in miles is", miles)


if __name__ == "__main__":
    main()
