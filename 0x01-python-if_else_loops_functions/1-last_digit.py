#!/usr/bin/python3
import random
number = random.randint(-10, 10)
last_digit = number % 10
str = f"Last digit of {number:d} is {last_digit:d}"
if last_digit == 0:
    print(f"{str} and is 0")
elif last_digit > 5:
    print(f"{str} and is greater than 5")
elif last_digit < 6 and not 0:
    print(f"{str} and is less than {6:d} and not {0:d}")
