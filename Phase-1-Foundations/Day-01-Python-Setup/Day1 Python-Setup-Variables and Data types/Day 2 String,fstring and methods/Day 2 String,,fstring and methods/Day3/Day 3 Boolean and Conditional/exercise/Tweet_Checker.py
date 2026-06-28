"""
Exercise  — Tweet Checker (solution).
"""

MAX_LEN = 280

tweet = input("Type your tweet: ")
length = len(tweet)

if not tweet:                       # empty string is falsy -> catch it first
    print("Your tweet is empty! Write something first.")
elif length <= MAX_LEN:             # 1..280 chars
    print(f"OK - good to post! ({length}/{MAX_LEN} chars)")
else:                               # too long
    over = length - MAX_LEN
    print(f"Too long by {over} characters ({length}/{MAX_LEN}). Trim it down.")