name = "Riya"
age = 25
height = 1.7

# ----- The old, clumsy way (with + and str()) -----
print("You are " + str(age) + " years old.")

# ----- The f-string way: prefix with f, use {curly braces} -----
print(f"You are {age} years old and {height}m tall.")

# ----- You can put any EXPRESSION inside the braces -----
print(f"Next year you'll be {age + 1}.")
print(f"Shouting your name: {name.upper()}")   # methods work too (next module)

# ----- Formatting numbers: add a : after the value -----
price = 2499.5
print(f"Price: Rs {price:.2f}")        # Rs 2499.50  -> always 2 decimals
print(f"Big number: {1000000:,}")      # 1,000,000   -> thousands separators
print(f"Total: Rs {price:,.2f}")       # Rs 2,499.50 -> both at once

gst = 0.18
print(f"GST rate: {gst:.0%}")          # 18%         -> percentage formatting

# ----- A mini receipt, all with f-strings -----
qty = 3
unit = 199.0
total = qty * unit
print(f"{qty} x Rs {unit:,.2f} = Rs {total:,.2f}")