#!/usr/bin/python3
if __name__ == "__main__":
    password = "Python is awesome"
    user_input = input()
    if user_input in password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
