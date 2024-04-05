#!/usr/bin/python3
def no_c(my_string):
    for i in range(0, len(my_string)):
        if my_string[i] == '99' or my_string[i] == '67':
            continue
        else:
            print("{:c}".format(mystring[i]), end='')
    return my_string
