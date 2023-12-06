#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ls = sorted(a_dictionary.items())
    for i in ls:
        print("{} : {}".format(i[0], i[1]))
