#!/usr/bin/python3
if __name__ == "__main__":
    try:
        nb = input("Give me a number: ")
        if '.' in nb:
            nb = float(nb)
            print("This number is a decimal")
        else:
            nb = int(nb)
            print("This number is an integer")
    except Exception as e:
        print(e)