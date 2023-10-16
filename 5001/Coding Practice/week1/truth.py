def main():   
    # header for the truth table
    print("+---+---+---+---+---+")
    print("| p | q | r | A | B |")

    # introduce three loop through all possible combinations of p, q, r
    for p in [False, True]:
        for q in [False, True]:
            for r in [False, True]:
                # determine the boolean values of A and B
                A = (p and q) or not r  
                B = not (p and (q or not r))

                # convert boolean values to 'F' or 'T'
                p_str = 'T' if p else 'F'
                q_str = 'T' if q else 'F'
                r_str = 'T' if r else 'F'
                A_str = 'T' if A else 'F'
                B_str = 'T' if B else 'F'

                # print the values in the table
                print("+---+---+---+---+---+")
                print(f"| {p_str} | {q_str} | {r_str} | {A_str} | {B_str} |")
    print("+---+---+---+---+---+")


if __name__ == "__main__":
    main()
