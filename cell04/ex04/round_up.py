#!/usr/bin/python3
import math

if __name__ == "__main__":
    try:
        nb = float(input("Give me a number: "))
        print(f'{math.ceil(nb)}')
    except Exception as e:
        print(e)