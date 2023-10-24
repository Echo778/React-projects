def main():
    score = float(input("Enter the score: "))
    print(grade(score))


def grade(score):
    if score > 92:
        return "A"
    elif 90 <= score <= 92:
        return "A-"
    elif 86 <= score <= 89:
        return "B+"
    elif 82 <= score <= 85:
        return "B"
    elif 77 <= score <= 81:
        return "B-"
    elif 73 <= score <= 77:
        return "C+"
    elif 69 <= score <= 72:
        return "C"
    elif 65 <= score <= 68:
        return "C-"
    elif 0 <= score <= 64:
        return "F"


if __name__ == "__main__":
    main()
