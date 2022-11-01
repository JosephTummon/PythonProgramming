# Get three numbers as input
# Check if number odd
# If odd check if max
num1 = int(input("Please enter the first integer: "))
num2 = int(input("Please enter the second integer: "))
num3 = int(input("Please enter the third integer: "))
max = 0

if num1 % 2 != 0:
    max = num1
if num2 % 2 != 0:
    if num2 > max:
        max = num2
if num3 % 2 != 0:
    if num3 > max:
        max = num3

if max == 0:
    print("These are all even numbers")
else:
    print(max)