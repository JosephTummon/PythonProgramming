# Create function
# Get input from user
# Create while loop to mkae sure non-negative input
# for loop in while loop to print out each case of function
# Get new input each time
# If while loop exited print finished
### *** Note, if you enter 1, it prints out two terms, because it was specified in sheet 0 is first term *** ###

def funct(x):
    #print("x is now:", x)
    if x == 0:
        return 13
    elif x == 1:
        return 8
    else:
        return (funct(x - 1) + 13 * funct(x - 2))

num = int(input("Please enter a non-negative number: "))
while num >= 0:
    for i in range(0, num + 1):
        print(funct(i), ", ", end="")
    print()
    num = int(input("Please enter a non-negative number: "))
print("Finished!")