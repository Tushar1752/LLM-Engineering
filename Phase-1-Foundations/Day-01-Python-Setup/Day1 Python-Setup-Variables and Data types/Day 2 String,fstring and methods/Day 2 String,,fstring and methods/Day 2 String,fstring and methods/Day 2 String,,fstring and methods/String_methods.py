text = "riya sharma"

# ----- Changing case -----
print(text.upper())      # RIYA SHARMA
print(text.lower())      # riya sharma
print(text.title())      # Riya Sharma  (capitalises each word)

# ----- IMPORTANT: methods return a NEW string; the original is unchanged -----
print("original is still:", text)   # riya sharma  (untouched)
loud = text.upper()
print("captured result:", loud)     # RIYA SHARMA

# ----- strip(): remove spaces (or newlines) from the ends -----
messy = "   hello world   "
print(f"[{messy.strip()}]")          # [hello world]

# ----- replace(old, new): swap text -----
year = "Event held in 2024"
print(year.replace("2024", "2025"))  # Event held in 2025

# ----- find() and count(): search inside a string -----
word = "hello"
print("index of first 'l':", word.find("l"))   # 2
print("number of 'l's:", word.count("l"))       # 2
print("'z' found at:", word.find("z"))           # -1  (not found)

# ----- startswith() / endswith(): True or False -----
email = "riya@gmail.com"
print("is a gmail?", email.endswith("@gmail.com"))   # True

# ----- Discover methods yourself: help(str.strip) in the REPL -----
print("\nTip: run  help(str.replace)  in the Python REPL to read the docs.")