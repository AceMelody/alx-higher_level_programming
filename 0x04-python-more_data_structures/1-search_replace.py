#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = my_list[:]
    for w in nlist:
        if w == search:
            idx = nlist.index(w)
            nlist[idx] = replace
        else:
            continue
    return nlist
