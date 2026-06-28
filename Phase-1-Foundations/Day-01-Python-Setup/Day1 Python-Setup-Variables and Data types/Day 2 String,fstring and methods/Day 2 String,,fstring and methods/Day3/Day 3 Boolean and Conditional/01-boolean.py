"""
Booleans — the True / False data type that powers every decision.
"""

# ----- There are exactly two boolean values. Note the capital T and F -----
is_raining = True
is_sunny = False
print(is_raining)                 # True
print(is_sunny)                   # False
print("type ->", type(is_raining))  # <class 'bool'>

# ----- GOTCHA: capitalisation matters. true / TRUE are NOT booleans -----
# print(true)   # ❌ NameError — Python doesn't know what `true` is
# Only True and False (capital first letter) are the real booleans.

# ----- "True" (in quotes) is a STRING, not a boolean -----
real_bool = True
fake_bool = "True"                # this is just text
print(type(real_bool))            # <class 'bool'>
print(type(fake_bool))            # <class 'str'>  <- very different!

# ----- Booleans usually come from a QUESTION (a comparison) -----
age = 20
is_adult = age >= 18             # the comparison evaluates to a boolean
print("Is adult?", is_adult)     # True

# ----- Under the hood: True is 1, False is 0 -----
# (You rarely rely on this, but it explains some surprising maths.)
print(True + True)               # 2
print(False + 10)                # 10
print(int(True), int(False))     # 1 0

# ----- bool() converts any value into True or False (preview of truthiness) -----
print(bool(1))                   # True
print(bool(0))                   # False
print(bool("hi"))                # True  (non-empty text)
print(bool(""))                  # False (empty text)