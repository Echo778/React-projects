import math


def main():
    length_1 = float(input("Enter first length of triangle: "))
    length_2 = float(input("Enter second length of triangle: "))
    length_3 = float(input("Enter third length of triangle: "))
    print(area_triangle(length_1, length_2, length_3))


def area_triangle(length_1, length_2, length_3):
    s = (length_1 + length_2 + length_3) / 2
    return math.sqrt(s * (s - length_1) * (s - length_2) * (s - length_3))


if __name__ == "__main__":
    main()
