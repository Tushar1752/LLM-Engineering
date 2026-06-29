"""
*args (extra positionals -> tuple) and **kwargs (extra keywords -> dict),
plus unpacking with * and ** at the call site.

"""


# 1) *args -> accept ANY number of positional arguments (as a tuple)
def total(*args):
    print("  args is a tuple:", args)
    return sum(args)

print("total(10, 20, 30) =", total(10, 20, 30))   # args == (10, 20, 30)
print("total(5)          =", total(5))             # args == (5,)
print("total()           =", total())              # args == () -> 0
print()

# 2) **kwargs -> accept ANY number of keyword arguments (as a dict)

def make_user(**kwargs):
    print("  kwargs is a dict:", kwargs)
    return kwargs

make_user(name="Asha", age=21, city="Pune")
make_user(name="Ben")
print()

# 3) Combine them — fixed param, then *args, then **kwargs
# A logger: a required message, optional extra values, optional context.
def log(message, *values, **context):
    line = message
    if values:
        line += " " + " ".join(str(v) for v in values)
    if context:
        extras = ", ".join(f"{k}={v}" for k, v in context.items())
        line += f"  [{extras}]"
    print(line)

log("Server started")
log("Processed items:", 1, 2, 3)
log("Request done", user="asha", status=200, ms=42)
print()
