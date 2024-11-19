#!/usr/bin/python3
if __name__ == "__main__":
    try:
        nb = int(input("Enter a number less than 25\n"))
        if nb > 25:
            print("Error")
            exit()
        for x in range(10):
            print(f"{x} x {nb} = {x * nb}")
    except Exception as e:
        print(e)