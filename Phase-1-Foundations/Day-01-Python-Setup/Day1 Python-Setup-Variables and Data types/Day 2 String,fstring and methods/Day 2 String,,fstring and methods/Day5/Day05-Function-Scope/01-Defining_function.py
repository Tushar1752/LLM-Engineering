"""
Defining functions — name a block of code once, reuse it forever.

"""


# 1) The simplest function: def name(): then an indented body

def greet():
    """Print a friendly greeting."""     # docstring = one-line description
    print("Hello, welcome to the course!")

# Defining did NOT run anything. The CALL (the parentheses) runs it:
greet()
greet()                                  # reuse — no copy-paste


# Bare name (no parens) is the function OBJECT, not a call:
print("greet without () is:", greet)     # <function greet at 0x...>

# 2) WHY functions: DRY (Don't Repeat Yourself)

# BEFORE — three near-identical blocks (notice the copy-paste smell):
print("Order #101 confirmed. A receipt was emailed to you.")
print("Order #102 confirmed. A receipt was emailed to you.")
print("Order #103 confirmed. A receipt was emailed to you.")
print()

# AFTER — one function, called three times (Module 02 adds the order id):
def confirm_order():
    """Print the standard order-confirmation message."""
    print("Order confirmed. A receipt was emailed to you.")

for _ in range(3):
    confirm_order()
print()

# 3) Docstrings power help() — try it

def area_of_circle():
    """Print the area of a circle with radius 5 (demo: no inputs yet)."""
    pi = 3.14159
    print(f"Area = {pi * 5 ** 2}")

area_of_circle()
# The docstring is readable at runtime — exactly how an AI agent later
# inspects a "tool" to decide whether to call it:
print("\nhelp text:", area_of_circle.__doc__)

# 4) Define BEFORE you call (order matters)

# This works because say_bye is defined above its call:
def say_bye():
    """Sign off."""
    print("See you tomorrow!")

say_bye()
# If you called say_bye() on a line ABOVE its def, Python would raise NameError.