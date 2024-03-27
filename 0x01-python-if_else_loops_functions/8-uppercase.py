#!/usr/bin/python3
def uppercase(str):
    for v in range(0, len(str)):
        w = ord(str[v])
        if w >= 97 and w <= 122:
            w = 65 + (97 - w)
            print("{:c}".format(w), end="")
        else:
            print("{}".format(w), end="")
