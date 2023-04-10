# Question1
num1 = 1
num2 = 2
num3 = 6
sum = num1 + num2 + num3
avg = sum/3
print("The average of three numbers is :", avg)

# Question2

# Inputs
gross_income = int(input("Enter gross income: "))
num_dependents = int(input("Enter number of dependents: "))

# Calculation of taxable income
standard_deduction = 10000
dependent_deduction = 3000
taxable_income = gross_income - standard_deduction - (dependent_deduction * num_dependents)

# Calculation of tax
tax_rate = 0.20
income_tax = taxable_income * tax_rate

# Final result
print("The income tax computes to: ", income_tax)

# Question 3

# type the number of seconds
seconds = int(input("Enter the number of seconds: "))

# Computing Minutes and seconds from seconds
minutes = seconds // 60
rem_seconds = seconds % 60

# Results of question 3
print("{} seconds is {} minutes and {} seconds,".format(seconds,minutes,rem_seconds))

# Question 4

a1 = 25
a2 = '25'
a3 = 25.0

# convert a2 to an integer
a2 = int(a2)

# Adding 3 A's
result = a1 + a2 + a3

# converting result into a string

result_str = str(result)

# print the result as a string
print(result_str)

# Question 5
import math

# Iterate over angles from 0 to 345 in 15 degree increments
for angle_degrees in range(0, 346, 15):
    # Convert angle to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate sine and cosine of angle
    sine = round(math.sin(angle_radians), 4)
    cosine = round(math.cos(angle_radians), 4)

    # Print results
    print(f"Angle: {angle_degrees} degrees, Sine: {sine}, Cosine: {cosine}")



