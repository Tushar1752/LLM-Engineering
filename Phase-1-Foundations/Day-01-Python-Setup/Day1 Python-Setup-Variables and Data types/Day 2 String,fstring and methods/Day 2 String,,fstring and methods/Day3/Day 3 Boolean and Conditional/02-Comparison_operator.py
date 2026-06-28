"""
Comparison & equality operators — questions that return a boolean.

"""


# ----- The six comparison operators all return True or False -----
print(5 > 3)        # True   greater than
print(5 < 3)        # False  less than
print(5 >= 5)       # True   greater than OR equal to
print(5 <= 4)       # False  less than or equal to
print(5 == 5)       # True   EQUAL TO  (note: double equals!)
print(5 != 3)       # True   NOT equal to

# ----- THE classic trap: = vs == -----
# =  assigns a value      (x = 5  means "put 5 into x")
# == asks a question      (x == 5 means "is x equal to 5?")
x = 5                # assignment
print(x == 5)        # True  -> comparison
# if x = 5:          # ❌ SyntaxError — you cannot assign inside a condition

# ----- Comparisons work on strings too (alphabetical / dictionary order) -----
print("apple" < "banana")   # True  ('a' comes before 'b')
print("Zoo" < "apple")      # True  (!) uppercase letters sort BEFORE lowercase
print("cat" == "Cat")       # False (capitalisation matters — case-sensitive)

# ----- Comparing ACROSS types -----
print(10 == 10.0)    # True   int and float compare by value
print(10 == "10")    # False  number vs string -> never equal
# print(10 < "10")   # ❌ TypeError — can't order a number against a string

# ----- A real-world feel: build a boolean from a comparison -----
password = "softpro123"
attempt = "softpro123"
print("Access granted?", password == attempt)   # True