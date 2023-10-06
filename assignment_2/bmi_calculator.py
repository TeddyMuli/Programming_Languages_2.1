print("****BMI CALCULATOR****")
name = input("Enter your name > ")
weight = int(input("Enter your weight in kg > "))
height = float(input("Enter your height in meters > "))
bmi = weight / (height**2)
if ((bmi >= 18.5) and (bmi <= 24.9)):
    status = "Normal Weight"
elif (bmi < 18.5):
    status = "Underweight"
elif ((bmi > 24.9) and (bmi < 30)):
    status = "Overweight"
else:
    status = "Obese"

print(f"Hi {name} your BMI is {bmi:.2f} and you are {status}")