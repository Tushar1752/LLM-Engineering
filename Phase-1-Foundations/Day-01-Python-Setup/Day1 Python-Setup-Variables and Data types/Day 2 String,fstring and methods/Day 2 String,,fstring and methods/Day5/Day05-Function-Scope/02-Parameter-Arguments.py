

# 1) One parameter -> feed the function different data each call
def greet(name):                     # `name` is the PARAMETER
    """Greet one person by name."""
    print(f"Hello, {name}!")

greet("Asha")                        # "Asha" is the ARGUMENT
greet("Ben")


# Arguments can be EXPRESSIONS, not just literals — Python evaluates first:
raw = "  chetan  "
greet(raw.strip().title())           # passes "Chetan"
print()


# 2) Upgrade Module 01's confirm_order to take the order id
def confirm_order(order_id):
    """Confirm a single order by id."""
    print(f"Order #{order_id} confirmed. Receipt emailed.")

for oid in [101, 102, 103]:
    confirm_order(oid)               # one definition handles every order

# 3) Multiple parameters -> matched by POSITION, left to right

def book_ticket(name, seat, price):
    """Print a booking line."""
    print(f"{name:<8} -> seat {seat:<4} (Rs {price})")

book_ticket("Asha", "12A", 850)
book_ticket("Ben", "12B", 850)
print()

# 4) REAL USE: a reusable GST/total calculator
def line_total(unit_price, quantity, gst_percent):
    """Print the GST-inclusive total for a line item."""
    subtotal = unit_price * quantity
    gst = subtotal * gst_percent / 100
    print(f"{quantity} x Rs {unit_price}"
          f"  + {gst_percent}% GST  =  Rs {subtotal + gst:.2f}")

line_total(199, 3, 18)               # 3 units at Rs 199, 18% GST
line_total(50, 10, 5)

# 5) The "swapped arguments" bug (positional order matters!)
print()
print("Correct order:")
book_ticket("Diya", "9C", 600)
print("Swapped (silent bug - no error, wrong result):")
book_ticket("Diya", 600, "9C")       # seat and price are reversed!
# Module 04's keyword arguments make this kind of mistake impossible.