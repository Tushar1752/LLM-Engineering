word = "Python"
#       012345

# ----- start:stop  (start included, stop EXCLUDED) -----
print("[0:3] ->", word[0:3])   # Pyt
print("[2:5] ->", word[2:5])   # tho

# ----- Leave a side blank to go to the very start / end -----
print("[:3]  ->", word[:3])    # Pyt   (from start)
print("[3:]  ->", word[3:])    # hon   (to end)
print("[:]   ->", word[:])     # Python (whole copy)

# ----- Negative slices: count from the end -----
print("[-3:] ->", word[-3:])   # hon   (last 3 chars)
print("[:-2] ->", word[:-2])   # Pyth  (everything except last 2)

# ----- The step: how many characters to jump -----
print("[::2] ->", word[::2])   # Pto   (every 2nd character)

# ----- The famous reverse trick: step of -1 -----
print("[::-1] ->", word[::-1]) # nohtyP  (reversed!)

# Slicing never errors on out-of-range bounds — it just stops at the edge:
print("[0:100] ->", word[0:100])  # Python