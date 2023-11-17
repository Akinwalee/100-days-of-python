weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = round(weight / (height ** 2))

if bmi < 18.5:
    print("Your BMI is {}, you are underweight.".format(bmi))
elif bmi < 25:
    print("Your BMI is {}, you are normal weight.".format(bmi))
elif bmi < 30:
    print("Your BMI is {}, you are slightly overweight.".format(bmi))
elif bmi < 35:
    print("Your BMI is {}, you are obese.".format(bmi))
else:
    print("Your BMI is {}, you are clinically obese.".format(bmi))