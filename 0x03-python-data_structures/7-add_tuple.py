#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    listed = []
    for n in range(0, len(tuple_a)):
        for p in range(0, len(tuple_b)):
            if p == n:
                elem = tuple_a[n] + tuple_b[p]
            else:
                continue
            listed.append(elem)
    new_tuple = tuple(listed)
    return new_tuple
