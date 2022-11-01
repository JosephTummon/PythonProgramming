# Get input from user
# Create function
# Using fiboacci function from p11p3.py, change num to x for substitution
# Use if else to run function if non-negative number is entered or print error if negative is.
num = int(input("Please enter a number to calculate the fibonacci sequence: "))

def fib(x):
    f_0 = 0
    f_1 = 1
    if x == 0:
        print("If number is 0, there will be no terms, enter a number greater than 0")
    elif x == 1:
        print("Series is:", f_0)
    elif x == 2:
        print("Series is:", f_0, f_1,)
    else:
        print("Series is: ", f_0, ", ", f_1, sep="", end="")
        for i in range(2, x):
            fib = f_0 + f_1
            print(",", fib, end="")

            f_0 = f_1
            f_1 = fib
        print()

if num >= 0:
    fib(num)
else:
    print("ERROR: Please enter a non-negative number.")