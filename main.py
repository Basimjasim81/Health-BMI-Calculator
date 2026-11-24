weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)
print(f"Your BMI is: {bmi:.1f}")

if bmi < 18.5:
    print("Underweight - need healthy nutrition")
elif bmi < 25:
    print("Normal - excellent")
elif bmi < 30:
    print("Overweight - need exercise")
else:
    print("Obese - consult doctor")
