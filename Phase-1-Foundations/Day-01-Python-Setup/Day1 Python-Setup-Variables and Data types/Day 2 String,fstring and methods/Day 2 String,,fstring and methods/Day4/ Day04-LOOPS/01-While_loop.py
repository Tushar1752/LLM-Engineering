"""
while loops — repeat a block WHILE a condition stays True.
"""



# 1) The anatomy: initialise -> test -> update
# =====================================================================
# Miss the UPDATE step and you loop forever. Point at all three parts:
count = 1                      # 1) initialise BEFORE the loop
while count <= 5:              # 2) test (checked before EVERY pass)
    print(f"Rep {count} of 5")
    count += 1                 # 3) update -> eventually makes the test False
print("Done counting.\n")

# A while-loop whose condition starts False runs ZERO times — that's fine:
stock = 0
while stock > 0:               # 0 > 0 is False, so the body never runs
    print("Selling an item")   # never prints
print("Nothing in stock to sell.\n")


# =====================================================================
# 2) REAL USE: a countdown timer (rocket launch / OTP expiry / cache TTL)
# =====================================================================
# while shines when you're counting DOWN to an event.
seconds = 5
while seconds > 0:
    print(f"Launching in {seconds}...")
    seconds -= 1               # update: walk toward the exit
print("Lift-off!\n")


# =====================================================================
# 3) REAL USE: process a work queue until it's empty
# =====================================================================
# This is exactly how a job runner / message consumer drains a backlog.
pending_orders = ["ORD-101", "ORD-102", "ORD-103"]
while pending_orders:                       # a non-empty list is truthy (Day 3!)
    order = pending_orders.pop(0)           # take the front item off the queue
    print(f"Processing {order} ... shipped. ({len(pending_orders)} left)")
print("All orders processed.\n")


# =====================================================================
# 4) REAL USE: accumulate until a threshold is crossed
# =====================================================================
# "Keep adding daily savings until we can afford the ₹15,000 phone."
target = 15000
saved = 0
day = 0
daily_saving = 2000
while saved < target:
    day += 1
    saved += daily_saving
    print(f"Day {day}: saved Rs {saved}")
print(f"Goal reached on day {day} with Rs {saved}.\n")


# =====================================================================
# 5) THE `while True:` + break IDIOM (previewing Module 04)
# =====================================================================
# An INTENTIONAL infinite loop you leave from the inside. This is the
# standard shape of a menu / REPL / chatbot turn-loop.
print("Tiny menu - type 'quit' to leave.")
while True:                                 # loop "forever"...
    choice = input("Pick (status / help / quit): ").strip().lower()
    if choice == "quit":
        print("Bye!")
        break                               # ...until we explicitly exit
    elif choice == "status":
        print("  All systems green")
    elif choice == "help":
        print("  Commands: status, help, quit")
    else:
        print(f"  Unknown command: {choice!r}")