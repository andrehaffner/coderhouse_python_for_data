
print("Welcome to BMI calculator!")
height = float(input("\nYour height in cm: "))
height = height/100
weight = float(input("\nYour weight in kg: "))
print("\nBMI:", {weight/height**2})
