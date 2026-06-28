"""
Exercise 1 — Magic Trick.

Steps (start with ANY number):
    1. Add 6
    2. Multiply by 2
    3. Subtract 4
    4. Divide by 2
    5. Subtract the original number
The result is always 4.

TODO: fill in the steps below, then run:
    python magic_trick.py
"""

number = 7
original =number
number +=6
number *=2
number -=4
number /=2
number -=original

print("Original number is ", original)
print("Number is ",number)