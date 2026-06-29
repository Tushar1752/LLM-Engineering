"""
Scope = where a variable is visible. Python searches L-E-G-B (first match wins).
"""

# G = GLOBAL: defined at the top level of the file.
app_name = "SSAI Tracker"


# 1) LOCAL: variables made inside a function live only there

def show_total():
    total = 999            # LOCAL — exists only while show_total() runs
    print("Inside  :", total)

show_total()
# print(total)             # would raise NameError: 'total' is not defined out here
print("Outside : total is invisible (it was local).\n")


# 2) READING a global from inside a function is fine
def banner():
    # No assignment to app_name -> Python finds it in GLOBAL scope (the G in LEGB).
    print(f"--- {app_name} ---")

banner()
print()

# 3) THE CLASSIC TRAP: assigning makes the name LOCAL for the whole function
count = 0

def bump_buggy():
    try:
        count = count + 1   # Python sees an assignment to `count` -> treats it
        print(count)        # as LOCAL everywhere in this function, so the READ
    except UnboundLocalError as e:   # on the right-hand side fails first.
        print("UnboundLocalError:", e)

print("Calling bump_buggy():")
bump_buggy()
print("(Module 06 shows the `global` keyword that fixes this.)\n")

# The non-buggy way without `global`: take it in, return it out.
def bump(n):
    return n + 1

count = bump(count)         # rebind the global ourselves, explicitly
count = bump(count)
print("count after two clean bumps:", count, "\n")

# 4) ENCLOSING scope (the E in LEGB) -> closures
def make_multiplier(factor):
    """Return a function that multiplies its input by `factor`."""
    def multiply(n):
        return n * factor   # `factor` lives in the ENCLOSING function's scope
    return multiply

triple = make_multiplier(3)
tenfold = make_multiplier(10)
print("triple(10) :", triple(10))     # 30 — remembers factor=3
print("tenfold(10):", tenfold(10))    # 100 — its own remembered factor
print()

# 5) BUILT-IN scope (the B) — and why you shouldn't shadow it
print("len('hello') uses the BUILT-IN len:", len("hello"))
# If you ever write `len = 5`, you HIDE the built-in and `len("x")` then crashes
# with 'int object is not callable'. Don't name variables list/dict/sum/len/type.