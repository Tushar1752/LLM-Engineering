"""
Logical operators — and / or / not. Combine booleans into one answer.
"""

# ----- and: True ONLY if BOTH sides are True -----
age = 25
income = 40000
print(age >= 18 and income >= 25000)   # True  (both pass)
print(age >= 18 and income >= 50000)   # False (second fails)

# ----- or: True if AT LEAST ONE side is True -----
is_weekend = False
is_holiday = True
print(is_weekend or is_holiday)        # True  (one is enough)
print(False or False)                  # False (need at least one True)

# ----- not: flips the boolean -----
print(not True)                        # False
print(not (age >= 18))                 # False  (age>=18 is True, not flips it)

logged_in = False
if not logged_in:                      # reads like English: "if not logged in"
    print("Please log in.")

# ----- Truth tables in one glance -----
print("--- and ---")
print(True and True, True and False, False and False)   # True False False
print("--- or ----")
print(True or True, True or False, False or False)      # True True False

# ----- PRECEDENCE: not > and > or  (and: think BODMAS for logic) -----
# Python evaluates `not` first, then `and`, then `or`.
print(True or False and False)         # True  -> 'and' binds first: True or (False) = True
# Use parentheses to make intent obvious and avoid bugs:
print((True or False) and False)       # False -> parentheses change the meaning

# ----- A realistic combo: discount eligibility -----
is_member = True
cart_total = 1200
first_order = False
gets_discount = is_member and (cart_total >= 1000 or first_order)
print("Gets discount?", gets_discount)   # True

# ----- Short-circuiting (bonus): Python stops as soon as the answer is known -----
# In `A and B`, if A is False, B is never even checked. In `A or B`, if A is True, B is skipped.
def expensive_check():
    print("  (expensive_check ran)")
    return True
print(False and expensive_check())     # expensive_check NEVER runs -> just prints False
print(True or expensive_check())       # expensive_check NEVER runs -> just prints True