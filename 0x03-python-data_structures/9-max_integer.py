#!/usr/bin/python3
def max_integer(my_list=[]):
    for m in range(0, len(my_list)):
        for n in range(0, len(my_list)):
            if m == n:
                continue
            else:
                if my_list[m] > my_list[n]:
                    maxint = my_list[m]
    return maxint
