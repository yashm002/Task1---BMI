user_height = float(input("Enter your height in centimeters: "))
user_weight = float(input("Enter your weight in kilograms: "))

user_bmi = user_weight / (user_height/100)**2
print("Your Body Mass Index (BMI) is", user_bmi)

if (user_bmi <= 18.5):
    print("You are underweight.")
    print("You are having minimal health risk.")

elif (user_bmi <= 24.9):
    print("You are healthy.")
    print("You have low health risk.")

elif (user_bmi <= 29.9):
    print("You are overweight.")
    print("You have high health risk.")

else:
    print("You are obese.")
    print("You should consult to doctor.")