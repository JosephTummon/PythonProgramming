# Get 3 numbers as input
# Put numbers in list
# Set max to 0
# Go through list
# If numer is odd check if it is max
# Also check if max is still zero in case number is negative
# At end if max is still 0 all numbers were even
# If not print what max is

num1 = int(input("Please enter the first integer: "))
num2 = int(input("Please enter the second integer: "))
num3 = int(input("Please enter the third integer: "))
list = [num1, num2, num3]
max = 0
for i in list:
    if i % 2 != 0:
        if i > max:
            max = i
        elif max == 0:
            max == i
if max == 0:
    print("These are all even")
else:
    print("The biggest odd number is:", max)

exit()