#!/usr/bin/python3
def elrment_at(my_list, idx):
    if idx >= 0:
        return my_list[idx]
    elif idx < 0 or idx >= len(my_list):
        return my_list
