#!/usr/bin/python3
if __name__ == "__main__":
    try:
        nb1 = int(input("Give me the first number: "))
        nb2 = int(input("Give me the second number: "))
        print("Thank you!")
        print(f"{nb1} + {nb2} = {nb1 + nb2}")
        print(f"{nb1} - {nb2} = {nb1 - nb2}")
        print(f"{nb1} / {nb2} = {nb1 / nb2}")
        print(f"{nb1} * {nb2} = {nb1 * nb2}")
    except Exception as e:
        print(e)
