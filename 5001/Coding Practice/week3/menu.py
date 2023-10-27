def menu():
    menu_list = ('''0 -- Quit
1 -- Add "O"
2 -- Add "oo"
3 -- Add "xXx"''')
    result = ""
    option = ""
    while (option != "0"):
        print(menu_list)
        option = input("Option: ")
        if option == "0":
            print("Result:", result)
        elif option == "1":
            result += "O"
        elif option == "2":
            result += "oo"
        elif option == "3":
            result += "xXx"
        else:
            print("Invalid option")


def main():
    menu()


if __name__ == "__main__":
    main()
