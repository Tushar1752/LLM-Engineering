"""
Truthiness / falsiness + the `in` operator.

Every value in Python is either "truthy" or "falsy" when used in a boolean
context (like an if-statement). And `in` checks membership.
"""

# ----- bool() reveals how a value behaves in an if-statement -----
# These are ALL the falsy values you'll meet this week:
print(bool(0))        # False  <- the number zero
print(bool(0.0))      # False  <- zero as a float
print(bool(""))       # False  <- an empty string
print(bool(None))     # False  <- the special "nothing" value (Day 2)
print(bool([]))       # False  <- an empty list (Day 6 preview)

# ----- Everything else is truthy -----
print(bool(1))        # True
print(bool(-5))       # True   <- ANY non-zero number, even negative
print(bool("hi"))     # True
print(bool("0"))      # True   <- careful! a NON-empty string, even "0", is truthy
print(bool(" "))      # True   <- a single space is non-empty -> truthy

# ----- Why this matters: you can test a value directly -----
name = input("Enter your name (or just press Enter): ")
if name:              # truthy if they typed something, falsy if empty
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name.")   # empty string is falsy

# ----- The `in` operator: is this INSIDE that? Returns a boolean -----
print("a" in "cat")          # True   substring check
print("z" in "cat")          # False
print("Cat" in "cat")        # False  (case-sensitive again!)
print("py" not in "python")      # True

# A very common real use: checking a keyword
sentence = "I love AI and machine learning"
print("AI" in sentence)      # True
print("blockchain" in sentence)  # False

# `not in` is the readable opposite
print("z" not in "cat")      # True