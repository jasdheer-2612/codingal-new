number = int(input("Enter the number:"))

if number % 2 == 0:
    print(number, "is even")

else:
    print(number, "is odd")

print("/n==================================n/")

height = float(input("Enter your height in meters"))
weight = float(input("Enter your weight in KG's"))

bmi = weight / (height ** 2)
print("BMI:", bmi)

if bmi <= 18.4:
    print("you are under weight")
elif bmi<= 24.9:
    print("you are healthy")
elif bmi <= 29.9:
    print("You are over weight")
elif bmi <= 34.9:
    print("you are severly over weight")
else:
    print("you are obese")

number = int(input("enter the number"))

if number > 50:
    print(number, "is greater than 50")
    if number % 2 == 0:
        print("and its even")
    else:
        print(number, "is odd" )
else:
    print(number, "is not greater than 50")




