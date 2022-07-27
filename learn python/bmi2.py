height = float(input('enter your height in meter: '))
weight = float(input('enter your weight in kg: '))
bmi = round(weight / height**2)
if bmi < 18.5:
    print(f'your bmi is {bmi}, you are underweight.')
elif bmi >= 18.5 and bmi < 25:
    print(f'your bmi is {bmi}, you have normal weight.')
elif bmi >= 25 and bmi < 30:
    print(f'your bmi is {bmi}, you are overweight.')
elif bmi >= 30 and bmi < 35:
    print(f'your bmi is {bmi}, you are obese.')
else:
    print(f'your bmi is {bmi}, you are clinically obese.')