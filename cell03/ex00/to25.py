#!/usr/bin/python3
if __name__ == "__main__":
    try:
        nb = int(input("Enter a number less than 25\n"))
        if nb > 25:
            print("Error")
            exit()
        while nb <= 25:
            print(f"Inside the loop, my variable is {nb}")
            nb += 1
    except Exception as e:
        print(e)