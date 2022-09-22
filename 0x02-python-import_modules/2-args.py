#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    i = 1
    args = len(argv)

    print(f"{args} {'argument' if args == 2 else 'arguments'}", end = "")
    print(f"{'.' if args == 1 else ':'}")
    while (i <= args):
        print(f"{i}: {argv[i]}")
        i += 1
