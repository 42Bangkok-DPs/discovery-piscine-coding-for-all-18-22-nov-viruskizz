#!/usr/bin/python3
if __name__ == "__main__":
    nb = input()
    if not nb.isdigit():
        print("This is not number")
        exit()
    nb = int(nb)
    if nb < 0:
        print("This number is negative")
    elif nb > 0:
        print("This number is positive")
    else:
        print("This number is both positive and negative")