#!/usr/bin/python3
if __name__ == "__main__":
    try:
        nb1 = int(input("Enter the first number:\n"))
        nb2 = int(input("Enter the second number:\n"))
        result = nb1 * nb2
        print(f'{nb1} x {nb2} = {result}')
        if result < 0:
            print("The result is negative")
        elif result > 0:
            print("The result is positive")
        else:
            print("The result is positive and negative")
    except Exception as e:
        print(e)