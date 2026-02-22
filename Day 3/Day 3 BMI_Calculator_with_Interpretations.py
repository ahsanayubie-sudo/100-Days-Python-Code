weight = int(input("What is your weight"))
height = int(input("What is your height "))

bmi = weight / (height ** 2)

if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")