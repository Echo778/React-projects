def main():
    hi = int(input("Enter larger: "))
    lo = int(input("Enter smaller: "))
    while lo >= hi:
        lo = int(input("Enter smaller: "))
    for i in range(hi, lo - 1, -1):
        print(i)


if __name__ == "__main__":
    main()
