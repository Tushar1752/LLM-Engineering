"""
break (quit the loop) and continue (skip this round), plus the loop-else.

"""

# 1) break -> stop as soon as we find what we want
# =====================================================================
# Search a list of orders for the first one over ₹1000, then STOP.
orders = [299, 150, 1499, 80, 5000]
for amount in orders:
    if amount > 1000:
        print(f"First big order found: Rs {amount} - stop searching.")
        break                       # no point scanning the rest
    print(f"  checked Rs {amount}, too small")
print()

# =====================================================================
# 2) continue -> skip the items we don't care about
# =====================================================================
# Sum only the POSITIVE transactions (skip refunds/negatives).
transactions = [500, -200, 1200, -50, 300]
income = 0
for t in transactions:
    if t < 0:
        continue                    # skip refunds, go to next transaction
    income += t                     # only positives reach this line
print(f"Total income (refunds skipped): Rs {income}\n")

# The "guard clause" style above keeps the main work un-nested. Compare:
#   for t in transactions:
#       if t >= 0:                  # everything ends up indented inside here
#           income += t

# =====================================================================
# 3) REAL USE: a retry loop with a limited number of attempts
# =====================================================================
# Verify a PIN: 3 attempts, break on success, lock out otherwise.
CORRECT_PIN = "1234"
attempts_left = 3
while attempts_left > 0:
    entered = input(f"Enter PIN ({attempts_left} tries left): ").strip()
    if entered == CORRECT_PIN:
        print("Access granted.")
        break                       # success -> leave the loop
    attempts_left -= 1              # wrong -> burn an attempt
    print("Wrong PIN.")
else:
    # while-else: runs only if the loop ended WITHOUT a break (i.e. ran out of tries)
    print("Card locked. Too many attempts.")
print()

# =====================================================================
# 4) The for-else: "searched everything, found nothing"
# =====================================================================
# Look up a username in our user list. The else runs only if we never broke.
users = ["asha", "ben", "chetan"]
target = "diya"
for u in users:
    if u == target:
        print(f"Welcome back, {u}!")
        break
else:
    print(f"No account for {target!r} - would you like to sign up?")