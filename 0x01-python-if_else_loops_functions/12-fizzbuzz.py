#!/usr/bin/python3

def fizzbuzz():
    """Function to print fizz, Buzz or fizzBuzz for multiples of 3&5"""
    for x in range(1, 101):
        if x % 15 == 0:
            print("FizzBuzz", end=" ")
        elif x % 5 == 0:
            print("Buzz", end=" ")
        elif x % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{}".format(x), end=" ")
