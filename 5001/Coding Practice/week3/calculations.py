def calculations():
    nums = int(input("Enter the number of values to read:"))
    total_sum = 0
    count = 0
    for i in range(nums):
        value = int(input("Enter an integer:"))
        total_sum += value
        count += 1
    if count > 0:
        average = total_sum / count
    else:
        average = 0
    print(f"The sum is {total_sum}")
    print(f"The average is {average}")


def main():
    calculations()


if __name__ == "__main__":
    main()
