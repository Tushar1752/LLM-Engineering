#Exercise 1 — Age Calculator.

name = input("Enter the name:")
birth_year = int(input("Please tell me your birth year:"))
current_year = int(2026)
age = current_year - birth_year
age = (f"{name} will turn {age} years in {2026}  ")
print(age)