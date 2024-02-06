#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        var = fct(*args)
        return var
    except (ValueError, ZeroDivisionError, TypeError, IndexError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stdrr)
        return None
