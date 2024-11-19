#!/usr/bin/python3
if __name__ == "__main__":
    nb = input()
    if nb.isdigit() and int(nb) == 0:
        print("This number is equal to zero")
    else:
        print("This number is different from zero")