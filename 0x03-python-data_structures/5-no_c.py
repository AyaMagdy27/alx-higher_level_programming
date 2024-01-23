#!/usr/bin/env python3
def no_c(my_string):
    rep = ""
    for l in range(len(my_string)):
        if (my_string[l] != 'c' and my_string[l] != 'C'):
            rep += my_string[l]
    return rep
