#!/usr/bin/python3
def add_tuple(tuple_a = (), tuple_b = ()):
    tup_list = []
    a_list = list(tuple_a)
    b_list = list(tuple_b)
    if len(a_list) < 2:
        a_list.append(0)
    if len(b_list) < 2:
        b_list.append(0)
    for w in range(0, 2):
        tup_list.append(a_list[w] + b_list[w])
    new_tup = tuple(tup_list)
    return new_tup
