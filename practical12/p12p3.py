# Set error to 0.1
# Get input from user
# Create root function
# Use root program from lecture 12, commmented guesses as not necessary for this assignmnet
# If statement to make sure num is non-negative
# Else print error message
error = 0.01
num = float(input("Please enter a number to calculate the root of: "))

def root(a, b):
    numguess = 0
    root = 0.0
    step = b  ** 2
    while abs(a - root ** 2) >= b and root ** 2 <= a:
        root += step
        numguess += 1
        #if numguess % 100000 == 0:
            #print("Still running. Number of guesses:", numguess)
    #print("Number of guesses:", numguess)
    if abs(a - root ** 2) < b:
        print("The approximate square root of", a, "is", root)
    else:
        print("Failed to calculate the square root of:", a)
if num >= 0:
    root(num, error)
else:
    print("ERROR: Please enter a non-negative number!")