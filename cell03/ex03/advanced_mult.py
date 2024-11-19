#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("none")
        exit()
    x = 0
    while x <= 10:
        print(f"Table  de {x}", end=" ")
        y = 0
        while y <= 10:
            print(x * y, end=" ")
            y += 1
        x += 1
        print()