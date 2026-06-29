# 1) return hands a value back; we can store and reuse it

def add(a, b):
    return a + b                  # give the result to whoever called us

total = add(2, 3)                 # capture it
print("add(2, 3) =", total)
print("reused   :", total * 10)   # 50 — only possible because we RETURNED
print()

# 2) THE BIG ONE: return vs print

def add_print(a, b):
    print(a + b)                  # shows the number, returns nothing

def add_return(a, b):
    return a + b                  # returns the number

p = add_print(2, 3)               # prints 5...
r = add_return(2, 3)              # ...returns 5
print("add_print returned:", p)   # None! (no return -> None)
print("add_return returned:", r)  # 5
# Try `p * 10` and you'd get: TypeError: unsupported operand type(s) None * int
print()

# 3) Early return ("guard clause") — handle the bad case, then bail

def safe_divide(a, b):
    """Return a/b, or a friendly message if b is 0."""
    if b == 0:
        return "Cannot divide by zero"   # bail early; lines below are skipped
    return a / b                          # happy path stays un-nested

print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))
print()

# 4) Return MULTIPLE values (Python packs them into a tuple)
def min_max_avg(numbers):
    """Return the min, max and average of a list of numbers."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

scores = [72, 95, 60, 88, 79]
low, high, avg = min_max_avg(scores)      # unpack the 3 returned values
print(f"low={low}  high={high}  avg={avg:.1f}")
print()

# 5) REAL USE: a pure helper you compose with others

# Pure functions (input -> return, no surprises) are easy to chain and test.
def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def describe_weather(fahrenheit):
    c = to_celsius(fahrenheit)            # reuse the return value of another fn
    label = "hot" if c >= 30 else "mild" if c >= 15 else "cold"
    return f"{fahrenheit}F = {c:.1f}C ({label})"

for f in [104, 68, 41]:
    print(describe_weather(f))