#!/usr/bin/python3
def fizzbuzz():
    for s in range(1, 101):
        if s % 3 == 0 and s % 5 == 0:
            print(f"FizzBuzz", end=" ")
        elif s % 3 == 0:
            print(f"Fizz", end=" ")
        elif s % 5 == 0:
            if s == 100:
                print(f"Buzz")
            else:
                print(f"Buzz", end=" ")
        else:
            print(f"{s:d}", end=" ")
