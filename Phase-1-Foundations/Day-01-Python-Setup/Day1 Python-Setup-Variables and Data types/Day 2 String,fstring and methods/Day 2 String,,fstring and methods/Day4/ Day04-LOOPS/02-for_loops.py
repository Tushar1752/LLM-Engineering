"""
for loops — run the body once for EACH item in a collection.
"""

# 1) Loop over a string -> one character at a time
# =====================================================================
for ch in "AI":
    print("Letter:", ch)
print()

# =====================================================================
# 2) Loop over a list -> one element at a time (the everyday case)
# =====================================================================
students = ["Asha", "Ben", "Chetan", "Diya"]
for student in students:                 # read it: "for each student in students"
    print(f"Welcome, {student}!")
print()

# =====================================================================
# 3) REAL USE: total up a column of numbers (an "accumulator")
# =====================================================================
cart_prices = [299, 1499, 49, 999]       # ₹ prices of items in a cart
total = 0                                 # start the running total at 0
for price in cart_prices:
    total += price                        # add each item to the total
print(f"Cart total: Rs {total}\n")

# =====================================================================
# 4) enumerate -> get the POSITION and the VALUE together
# =====================================================================
# Perfect for numbered menus, leaderboards, "line 5 of the file", etc.
leaderboard = ["Asha", "Ben", "Chetan"]
for rank, name in enumerate(leaderboard, start=1):   # start counting at 1, not 0
    print(f"#{rank}  {name}")
print()

# Compare: the clumsy manual-counter version enumerate replaces.
# i = 1
# for name in leaderboard:
#     print(i, name)
#     i += 1          # easy to forget / put in the wrong place

# =====================================================================
# 5) REAL USE: validate / filter as you go
# =====================================================================
# Loop over signup emails and flag the ones that look invalid.
emails = ["asha@gmail.com", "broken-email", "ben@yahoo.com", "@oops"]
for email in emails:
    looks_valid = "@" in email and "." in email and not email.startswith("@")
    status = "ok" if looks_valid else "check this"
    print(f"{email:<22} {status}")
print()

# =====================================================================
# 6) REAL USE: build a NEW list from an old one (transform each item)
# =====================================================================
# Apply a 10% discount to every price. This "build a new list" shape is
# everywhere in data work (and is what a list comprehension shortens later).
discounted = []
for price in cart_prices:
    discounted.append(round(price * 0.9, 2))
print("Original  :", cart_prices)
print("Discounted:", discounted)

# After the loop ends, the loop variable keeps its LAST value:
print("\nLast price seen by the loop variable:", price)