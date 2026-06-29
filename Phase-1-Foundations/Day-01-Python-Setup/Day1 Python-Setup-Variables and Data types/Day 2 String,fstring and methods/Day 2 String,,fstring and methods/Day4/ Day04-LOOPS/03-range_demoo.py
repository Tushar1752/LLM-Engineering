"""
range() — generate numbers to loop over. Three forms: stop / start,stop / start,stop,step.

"""

# 1) range(stop) -> 0 .. stop-1   (stop is EXCLUDED)
# =====================================================================
print("range(5) gives:", list(range(5)))      # [0, 1, 2, 3, 4]  -> NOT 5!

# The most common use: "do this N times" — the number itself is ignored.
for _ in range(3):                             # _ = "I don't care about the value"
    print("  ping")
print()

# =====================================================================
# 2) range(start, stop) -> inclusive start, exclusive stop
# =====================================================================
# To loop 1..10 INCLUSIVE you must say range(1, 11):
print("Multiplication table for 7:")
for n in range(1, 11):                         # 1, 2, ... 10  (note the 11!)
    print(f"  7 x {n} = {7 * n}")
print()

# =====================================================================
# 3) range(start, stop, step) -> jump by `step`
# =====================================================================
print("Evens 0..10 :", list(range(0, 11, 2)))   # [0, 2, 4, 6, 8, 10]
print("By tens     :", list(range(0, 101, 10)))  # [0, 10, ... 100]

# Negative step = countdown (a real launch / quiz timer):
print("Countdown:")
for t in range(5, 0, -1):                        # 5, 4, 3, 2, 1
    print(f"  {t}...")
print("  GO!\n")

# =====================================================================
# 4) REAL USE: paginate results 20 at a time
# =====================================================================
# API/search results come back in pages. range with a step models the offsets.
total_results = 95
page_size = 20
for offset in range(0, total_results, page_size):
    page_no = offset // page_size + 1
    last = min(offset + page_size, total_results)   # don't run past the end
    print(f"Page {page_no}: showing results {offset + 1}-{last}")
print()

# =====================================================================
# 5) REAL USE: compute a running balance with simple interest
# =====================================================================
# "If I invest ₹10,000 at 8%/year, what's the balance each year for 5 years?"
balance = 10_000
rate = 0.08
for year in range(1, 6):                         # years 1 through 5
    balance += balance * rate
    print(f"End of year {year}: Rs {balance:,.2f}")