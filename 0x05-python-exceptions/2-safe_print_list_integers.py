#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for items in range(x):
        try:
            print("{:d}".format(my_list[items]), end='')
            n += 1
        except (ValueError, TypeError):
            pass
    print()
    return n
