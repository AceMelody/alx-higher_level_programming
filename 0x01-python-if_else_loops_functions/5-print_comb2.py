#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if (x != 9 and y <= 9) or (x == 9 and y < 9):
            print("{:d}{:d}, ".format(x, y), end=" ")
        elif x == 9 and y == 9:
            print("{:d}{:d}".format(x, y))
