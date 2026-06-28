messy_name = "   Riya Sharma   "

# ----- One step at a time (verbose) -----
step1 = messy_name.strip()       # "Riya Sharma"
step2 = step1.upper()            # "RIYA SHARMA"
step3 = step2.replace(" ", "_")  # "RIYA_SHARMA"
print("step by step:", step3)

# ----- The same thing, CHAINED (reads left to right) -----
result = messy_name.strip().upper().replace(" ", "_")
print("chained:     ", result)   # RIYA_SHARMA

# ----- Real-world clean-up: tidy a messy user entry -----
user_input = "  ALICE@Example.COM  "
clean_email = user_input.strip().lower()
print("clean email:", clean_email)   # alice@example.com

# ----- split(): break a string into a list of pieces -----
csv_row = "Riya,Mumbai,25"
parts = csv_row.split(",")
print("split ->", parts)          # ['Riya', 'Mumbai', '25']
print("city is:", parts[1])       # Mumbai

# ----- join(): glue a list of pieces back into one string -----
words = ["AI", "is", "fun"]
sentence = " ".join(words)
print("join ->", sentence)        # AI is fun
print("dashes ->", "-".join(words))   # AI-is-fun