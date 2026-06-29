"""
Default values + keyword arguments, and the famous mutable-default trap.
"""


# 1) Default values -> make a parameter optional
def greet(name, greeting="Hi"):          # greeting has a fallback
    print(f"{greeting}, {name}!")

greet("Asha")                            # uses the default -> "Hi, Asha!"
greet("Ben", "Good morning")             # overrides it
print()

# Real-world defaults: configuration with sensible fallbacks.
def connect(host, port=5432, timeout=30):
    print(f"Connecting to {host}:{port} (timeout {timeout}s)")

connect("db.example.com")                # most calls accept the defaults
connect("db.example.com", port=6543)     # override just one
print()

# 2) Keyword arguments -> order stops mattering, calls self-document

def book_ticket(name, seat, price):
    print(f"{name} -> seat {seat} (Rs {price})")

book_ticket(name="Asha", price=850, seat="12A")   # any order, totally clear
# This makes the Module 02 "swapped arguments" bug impossible.

# You CAN mix, but positional args must come first:
book_ticket("Ben", price=600, seat="9C")
print()

# 3) THE MUTABLE DEFAULT TRAP  (a famous Python gotcha)

def add_item_buggy(item, cart=[]):       # the [] is created ONCE and shared!
    cart.append(item)
    return cart

print("Buggy version (state leaks between calls):")
print(" ", add_item_buggy("apple"))      # ['apple']
print(" ", add_item_buggy("milk"))       # ['apple', 'milk'] <- leaked!
print(" ", add_item_buggy("bread"))      # ['apple', 'milk', 'bread']
print()

# The fix: default to None, create a fresh list inside.
def add_item(item, cart=None):
    if cart is None:
        cart = []                        # brand-new list every call
    cart.append(item)
    return cart

print("Fixed version (independent each call):")
print(" ", add_item("apple"))            # ['apple']
print(" ", add_item("milk"))             # ['milk']
print()

# 4) REAL USE: this is exactly the shape of an LLM API call
# In Phase 1 you'll write calls like this constantly — keyword args + defaults.
def generate(prompt, model="gemini-1.5-flash", temperature=0.7, max_tokens=512):
    """Pretend LLM call — just describes the request it would send."""
    return (f"[{model}] temp={temperature} max_tokens={max_tokens}\n"
            f"  prompt: {prompt!r}")

print(generate("Summarise this article"))                       # all defaults
print(generate("Write a poem", temperature=1.2, max_tokens=200))  # override two