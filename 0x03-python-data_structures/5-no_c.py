#!/usr/bin/env python3
def no_c(my_string):
    replace = ""
    for l in range(len(my_string)):
        if (my_string[l] != 'c' and my_string[l] != 'C'):
            replace += my_string[l]
    return replace
