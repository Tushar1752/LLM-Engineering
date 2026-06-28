word = "Hello"

# ----- Positive indexing starts at 0 -----
print("first  char [0]  ->", word[0])   # H
print("third  char [2]  ->", word[2])   # l
print("fifth  char [4]  ->", word[4])   # o

# ----- Negative indexing counts from the end -----
print("last   char [-1] ->", word[-1])  # o
print("2nd last  [-2]   ->", word[-2])  # l

# ----- Out-of-range index raises an error -----
# print(word[10])        #  IndexError: string index out of range (uncomment to see)

# ----- Strings are IMMUTABLE: you can read but not change a character -----
print("read word[0]:", word[0])
# word[0] = "J"          #  TypeError: 'str' object does not support item assignment
new_word = "J" + word[1:]   # instead, build a NEW string (slicing covered next module)
print("rebuilt word:", new_word)   # Jello

# ----- The special value None: "nothing here" -----
result = None
print("result is:", result)        # None
print("type of None ->", type(result))   # <class 'NoneType'>