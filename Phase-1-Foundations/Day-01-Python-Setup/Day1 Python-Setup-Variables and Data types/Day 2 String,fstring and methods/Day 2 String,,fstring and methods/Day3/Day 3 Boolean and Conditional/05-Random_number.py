"""
Generating random numbers with the `random` module + conditionals.
"""


import random        # 'import' pulls in extra tools (full lesson on Day 7)

# ----- randint(a, b): a random WHOLE number, both ends INCLUDED -----
roll = random.randint(1, 6)        # could be 1, 2, 3, 4, 5, or 6
print("You rolled:", roll)

# ----- Run it a few times — the value changes each run -----
print("Three more rolls:", random.randint(1, 6),
      random.randint(1, 6), random.randint(1, 6))

# ----- Other handy random tools -----
print("Random pick:", random.choice(["rock", "paper", "scissors"]))  # pick from a list
print("Random %:", random.randint(0, 100))

# ----- Combine random + conditionals: a coin flip -----
flip = random.randint(0, 1)        # 0 or 1
if flip == 0:
    print("Coin: HEADS")
else:
    print("Coin: TAILS")

# ----- A tiny "lucky number" game -----
secret = random.randint(1, 3)
guess = int(input("Guess my number (1-3): "))
if guess == secret:
    print(f"Correct! It was {secret}.")
else:
    print(f"Nope - I was thinking of {secret}.")

# ----- Reproducible randomness: seed it (great for testing) -----
random.seed(42)                    # same seed -> same "random" sequence every run
print("Seeded roll:", random.randint(1, 100))   # always the same now