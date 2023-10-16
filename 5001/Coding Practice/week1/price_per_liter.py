def main(): 
    # input the price of a six-pack of soda and the price of a two-liter bottle
    six_pack_price = float(input("Price per six-pack:"))
    two_liter_price = float(input("Price per two-liter:"))

    # calculate the price per liter for both options
    six_pack_price_per_liter = six_pack_price / (6 * 0.355)
    two_liter_price_per_liter = two_liter_price / 2.0

    # output the results
    print("Six-pack price per liter:", six_pack_price_per_liter)
    print("Two-liter price per liter:", two_liter_price_per_liter)


if __name__ == "__main__":
    main()
