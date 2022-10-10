#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for i in range(x):
        try:
            if isinstance(int(my_list[i]), int):
                print("{:d}".format(my_list[i]), end="")
            c += 1
        except (IndexError):
            print("IndexError: list index out of range")
            return
    print()
    return
