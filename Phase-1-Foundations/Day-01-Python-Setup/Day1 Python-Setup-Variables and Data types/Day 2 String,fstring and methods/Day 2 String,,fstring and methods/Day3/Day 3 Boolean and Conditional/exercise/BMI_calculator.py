height=float(input("Enter the height of the person in metres:"))
weight=float(input("Enter the weight of person in kg:"))
bmi = weight/(height)**2

print(f"your bmi is {bmi} and your category is :")
if bmi<18.5:
    print("you are underwight")
elif 18.5 <= bmi <25:
    print("You are normal ")
elif 25 <= bmi < 30:
    print("You are overweight")
else:
    print("Obese")





"""
Exercise  — BMI Calculator (STUDENT STUB).

BMI = weight(kg) / height(m)^2
Categories:
    BMI < 18.5            -> Underweight
    18.5 <= BMI < 25      -> Normal
    25   <= BMI < 30      -> Overweight
    BMI >= 30            -> Obese

"""