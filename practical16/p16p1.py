# Create function
# Get input from user
# Use while loop to start when number greater than or equal to one
# Call number in for-loop to print up to num+ 1
# Print each number
# Get new input that will restart loop if greater than or equal to one

def myfunction (x):
    """Function to calculate 2 * f(x - 1) with base case f(1) = 2"""
    print("x is now:", x)
    if x == 1:
        return 2
    else:
        return 2 * (myfunction(x - 1))
print(myfunction(4))

num = int(input("Please enter number to enter into the function: "))

while num >= 1:
    for i in range(1, num + 1):
        print(myfunction(i), ", ", end="")
    print("")
    num = int(input("Please enter number to enter into the function: "))
print("Finished!")