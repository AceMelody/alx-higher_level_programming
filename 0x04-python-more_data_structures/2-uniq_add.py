#!/usr/bin/python3
def uniq_add(my_list=[]):
    for x in my_list:
        for y in range(len(my_list)):
            if my_list.index(x) == y:
                continue
            else:
                if my_list[y] == x:
                    my_list.remove(x)
                    break
    add = sum(my_list)
    return add
