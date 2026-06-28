# ----- \n makes a new line -----
print("Line 1\nLine 2")        # two lines

# ----- \t inserts a tab -----
print("Name:\tRiya")           # Name:   Riya
print("Score:\t98")

# ----- \" and \' let you put quotes inside the same kind of quotes -----
print("She said \"hi\"")       # She said "hi"
print('It\'s fine')            # It's fine

# ----- \\ is a single literal backslash -----
print("A backslash: \\")       # A backslash: \

# ----- Windows path gotcha: \n inside a path! -----
# print("C:\name")             # the \n becomes a new line
print("Safe path:", "C:\\Users\\Riya")   # double the backslashes
print("Raw string:", r"C:\Users\Riya")   # or use r"..." to switch escaping OFF

# ----- Triple quotes: multi-line text, written as-is -----
prompt = """You are a helpful assistant.
Summarise the text below in 3 bullet points.
Keep it under 50 words."""
print("\n--- An LLM prompt (multi-line) ---")
print(prompt)















