# ----- Making strings: single or double quotes both work -----
greeting = 'Hello'
name = "Riya"
print(greeting)
print(name)
print("type of a string ->", type(greeting))   # <class 'str'>

# ----- Quotes inside quotes: pick the OTHER quote on the outside -----
print("it's a sunny day")          # ' inside, so wrap in "
print('She said "hi" to me')       # " inside, so wrap in '

# ----- Concatenation: join strings with + -----
full = "AI" + " " + "Engineer"     # spaces don't appear unless you add them
print(full)                        # AI Engineer

first = "Riya"
last = "Sharma"
print("Full name:", first + " " + last)

# ----- Repetition: repeat a string with * -----
print("ha" * 3)                    # hahaha
print("=" * 20)                    # a nice divider line: ====================

# ----- Gotcha: you can't add a string and a number directly -----
age = 25
# print("Age: " + age)            # ❌ TypeError — uncomment to see the error
print("Age: " + str(age)) 