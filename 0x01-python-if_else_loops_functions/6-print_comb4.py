#!/usr/bin/python3
for d in range(0, 10):
    for g in range(0, 10):
        if g > d:
            print("{:d}{:d}".format(d, g), end="")
            if (d < 8 and g <= 9) or (d == 8 and g < 9):
                print(f",", end=" ")
            elif d == 8 and g == 9:
                print("")
