weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = round(weight / (height ** 2))

print("Your BMI is {}".format(bmi))