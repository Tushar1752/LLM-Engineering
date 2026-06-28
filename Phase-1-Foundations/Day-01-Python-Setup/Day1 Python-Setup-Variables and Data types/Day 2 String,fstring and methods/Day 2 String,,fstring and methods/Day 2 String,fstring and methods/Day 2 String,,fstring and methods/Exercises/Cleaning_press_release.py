"""
 Press Release clean-up.

Turn a messy headline into a tidy one using string methods + chaining. """

raw = "   softpro school of ai LAUNCHES new 45-day ai program!!!   "
cleaned = raw.strip().replace("!!!","").title()
print("BEfore Cleaning:", raw)
print("After cleaning:", cleaned)

print(f"character before cleaning were {len(raw)} and after cleaning were {len(cleaned)}")