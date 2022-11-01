# Create function for factorial
# set a to 1 and i to 1
# Create for loop that multiplies a by i, then adds one to i
# a will be the factorial when finished
# Use if else statement to only run function is non-negative is entered
def fact(x):
    a = 1
    i = 1
    while i <= x:
        a *= i
        i += 1
    return(a)

num = int(input("Please enter a number to calculate the factorial: "))           
if num >= 0:
    print("The factorial of", num, "is", fact(num))
else:
    print("Error, please enter a non-negative integer.")
exit()
