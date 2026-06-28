"""
Conditionals — if / elif / else. This is where programs start to "decide".
"""


temperature = 38
if temperature > 35:
    print("It's a hot day, stay hydrated!")   # 4-space indent = "inside the if"

print("This line always runs (it's not indented).")

# ----- if / else: one of two paths ALWAYS runs -----
age = 16
if age >= 18:
    print("You can vote.")
else:
    print("Too young to vote - wait a bit!")

# ----- if / elif / else: pick ONE path from many (checked top to bottom) -----
# elif = "else if". You can have as many elifs as you like.
marks = 72
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"        # 72 lands here -> stops checking the rest
elif marks >= 40:
    grade = "D"
else:
    grade = "F"
print(f"Marks {marks} -> Grade {grade}")

# ----- KEY IDEA: only the FIRST matching branch runs, then Python skips the rest -----
# Order matters! If we checked `marks >= 40` first, 72 would wrongly become "D".

# ----- Indentation IS the syntax (Python has no { } braces) -----
# Everything indented under the `if` belongs to it. Mixing tabs/spaces breaks this.
balance = 5000
if balance >= 1000:
    print("Premium customer")
    print("  - free delivery")     # both indented lines run together
    print("  - priority support")
print("Thanks for visiting!")      # un-indented -> always runs