#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if x < 9 or (x == 9 and y < 9):
            print(f"{x:d}{y:d}, ", end=" ")
        else:
            print(f"{x:d}{y:d}")
