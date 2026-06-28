
# ----- len(): how many characters? -----
print("len('Python') =", len("Python"))   # 6
print("len('') =", len(""))                # 0

# ----- input() ALWAYS returns a string -----
name = input("What's your name? ")
print("Nice to meet you,", name)
print("Your name has", len(name), "characters.")

# ----- Type casting: input is text, so convert before doing maths -----
age_text = input("How old are you? ")      # e.g. "25"  (a string!)
print("type of what you typed ->", type(age_text))   # <class 'str'>

age = int(age_text)                        # convert "25" -> 25
print("Next year you'll be", age + 1)

# ----- str() goes the other way: number -> text (so you can join with +) -----
print("You are " + str(age) + " years old.")

# ----- float() for decimals -----
height = float(input("Your height in metres (e.g. 1.7)? "))
print("Half your height is", height / 2, "m")