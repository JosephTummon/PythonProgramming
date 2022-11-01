# Create function
# get input from user
# While input positive
# Use for loop in while loop to print out each number
# Have print statement commented to see progress towards base case
# If while loop exited it is because of negative number
def funct(x):
    if x == 1:
        return 2
    else:
        # print("x is now", x)
        return(x + funct(x - 1))
num = int(input("Please enter a number greater than or equal to one: "))
while num > 0:
    for i in range(num):
        print(funct(i + 1), ", ", end="")
    print()
    num = int(input("Please enter a number greater than or equal to one: "))
print("Negative number enterred")