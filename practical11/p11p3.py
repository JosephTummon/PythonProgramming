# Used method we went through in lecture
# Set up while loop, intialise f_0 and f_1 at start of every loop
# No series for 0, but we only want program to stop for negative, so say no series then move on if num = 0
# print for num = 1 or 2
# if num > 2, use for loop
# Same as lecture notes, but removed a and b variable and just keep f_0 and f_1
# If while loop exited means negative number was entered

num = int(input("How many terms would you like me to calculate: "))
while num >= 0:
    f_0 = 0
    f_1 = 1
    if num == 0:
        print("If number is 0, there will be no terms, enter a number greater than 0")
    elif num == 1:
        print("Series is:", f_0)
    elif num == 2:
        print("Series is:", f_0, f_1,)
    else:
        print("Series is: ", f_0, ", ", f_1, sep="", end="")
        for i in range(2, num):
            fib = f_0 + f_1
            print(",", fib, end="")

            f_0 = f_1
            f_1 = fib
        print()
    num = int(input("How many terms would you like me to calculate: "))
print("This number is not positive!")
print("Finished!")