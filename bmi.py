weight = int(input("Enter your weight : "))
height = float(input("Enter your height : "))

bmi = weight / (height ** 2)
if bmi<18.5:
    print("underweight")
elif 18.5<=bmi<25:
    print("normal weight")
else:
    print("overweight")
