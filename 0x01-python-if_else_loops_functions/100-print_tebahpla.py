#!/usr/bin/python3
for k in reversed(range(97, 123)):
    if (k % 2 == 0):
        print(f"{k:c}", end="")
    else:
        k = 65 + (k - 97)
        print(f"{k:c}", end="")
