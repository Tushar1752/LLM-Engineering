"""
Nesting conditionals — an if INSIDE another if.
"""

age = 20
has_ticket = True

if age >= 18:                          # outer gate
    print("Age check passed.")
    if has_ticket:                     # inner gate (8-space indent)
        print("Welcome to the concert!")
    else:
        print("You're old enough, but you need a ticket.")
else:
    print("Sorry, 18+ event.")

# ----- The same logic often reads better FLATTENED with `and` (preview of Module 07) -----
# if age >= 18 and has_ticket:
#     print("Welcome to the concert!")
# Use nesting when the inner checks only make sense after the outer one passes,
# or when each level needs its own different message.

print("-" * 30)

# ----- A practical example: login + role -----
logged_in = True
role = "admin"

if logged_in:
    print("Login OK.")
    if role == "admin":
        print("Showing admin dashboard.")
    elif role == "editor":
        print("Showing editor tools.")
    else:
        print("Showing read-only view.")
else:
    print("Please log in first.")     # if not logged in, role doesn't even matter

# ----- Watch the indentation levels: 0 -> 4 -> 8 spaces -----
# Level 0: the outer if
#     Level 4: code inside outer if
#         Level 8: code inside the inner if