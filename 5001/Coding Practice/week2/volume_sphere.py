def main():
    radius = float(input("Enter radius of sphere: "))
    print(volume_sphere(radius))


def volume_sphere(radius):
    return (4 / 3) * 3.14159 * (radius ** 3)


if __name__ == "__main__":
    main()
