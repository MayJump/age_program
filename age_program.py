def print_age_elagibility(n1, a1, n2, a2):
    in1 = 18 <= a1 <= 64
    in2 = 18 <= a2 <= 64
    if in1 and in2:
        return "BOTH\nBoth people are between 18 and 64"
    elif not (in1 or in2):
        return "NEITHER\nNeither person is between 18 and 64"
    else:
        if in1:
            return "ONE\n" + f"{n1} is between 18 and 64, but {n2} is not."
        else:
            return "ONE\n" + f"{n2} is between 18 and 64, but {n1} is not."

def main():
    p1 = input("Please enter the name of one person: ")
    a1 = int(input(f"Please enter {p1}'s age: "))
    p2 = input("Please enter the name of another person: ")
    a2 = int(input(f"Please enter {p2}'s age: "))
    print(print_age_elagibility(p1, a1, p2, a2))

if __name__ == "__main__":
    main()
