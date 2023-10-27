def main():
    a = 0
    b = 1
    print("0\n1")
    c = a + b
    while (c < 1000):
        c = a + b
        print(c)
        a, b = b, c


main()
