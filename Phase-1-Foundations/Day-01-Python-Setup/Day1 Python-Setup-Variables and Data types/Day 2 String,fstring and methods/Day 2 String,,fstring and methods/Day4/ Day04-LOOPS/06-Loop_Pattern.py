


import random

random.seed(42)   # fixed seed -> the "random" demos print the same every run

sales = [1200, 450, 3300, 80, 1500, 999, 2750]   # ₹ daily sales we'll analyse


# PATTERN 1 — ACCUMULATE: running total / max / min

total = 0                       # start at the additive identity
highest = sales[0]              # seed max/min with the first real value
for amount in sales:
    total += amount             # fold each value into the running total
    if amount > highest:        # ...and track the biggest seen so far
        highest = amount
print(f"Total sales : Rs {total}")
print(f"Best day    : Rs {highest}")
print(f"Average     : Rs {total / len(sales):.2f}")
# (Python ships sum()/max()/min() that do this for you — but THIS is what
#  they're doing under the hood. Knowing the long form is the point.)
print()


# PATTERN 2 — COUNT: how many items match a condition?

big_days = 0
for amount in sales:
    if amount >= 1000:          # the "matches?" test
        big_days += 1           # count = accumulate + 1
print(f"Days over Rs 1000: {big_days} of {len(sales)}\n")


# PATTERN 3 — SEARCH + FLAG: is there one? which is the first?


target = 999
position = -1                   # -1 = "not found yet"
for index, amount in enumerate(sales):
    if amount == target:
        position = index
        break                   # found it -> stop searching
if position >= 0:
    print(f"Rs {target} first appears on day {position + 1}.")
else:
    print(f"Rs {target} never appears.")
print()

# PATTERN 4 — BUILD: make a NEW collection from an old one

# Tag each day as 'good' or 'slow' -> build a parallel list of labels.
labels = []                     # start empty
for amount in sales:
    labels.append("good" if amount >= 1000 else "slow")
print("Day labels:", labels)
# This "start empty, append each pass" shape is exactly what a list
# comprehension shortens:  labels = ["good" if a >= 1000 else "slow" for a in sales]
print()


# PATTERN 5 — RETRY: keep trying until success (or give up) — VERY AI-relevant

# Model APIs / network calls fail transiently. Standard fix: retry with a cap
# and growing wait ("exponential backoff"). We simulate the flaky call here.
def flaky_api_call():
    """Pretend network call: fails ~60% of the time."""
    return random.random() > 0.6        # True = success

MAX_ATTEMPTS = 5
for attempt in range(1, MAX_ATTEMPTS + 1):
    print(f"Attempt {attempt}...", end=" ")
    if flaky_api_call():
        print("success!")
        break                            # got a response -> stop retrying
    wait = 2 ** (attempt - 1)            # backoff: 1, 2, 4, 8 ... seconds
    print(f"failed, would wait {wait}s before retrying")
    # In real code: import time; time.sleep(wait)   (skipped so the demo is instant)
else:
    # for-else: ran out of attempts without a single success
    print("Giving up after all retries - alert the on-call engineer.")