#!/usr/bin/python3
if __name__ == "__main__":
    try:
        age = int(input("Please tell me your age: "))
        print(f"You are currently {age} years old.")
        print(f"In 10 years, you'll be {age + 10} years old.")
        print(f"In 20 years, you'll be {age + 20} years old.")
        print(f"In 30 years, you'll be {age + 30} years old.")
    except Exception as e:
        print(e)