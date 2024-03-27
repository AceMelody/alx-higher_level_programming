#!/usr/bin/python3
for v in range(0, 10):
    for w in range(0, 10):
        if v < w:
            print(f"{v:d}{w:d}", end="")
            if v < 8 and w < 10:
                print(f",", end=" ")
            else:
                print("")
