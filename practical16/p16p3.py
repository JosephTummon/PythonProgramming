# Create function for divisors 
# Instead of tuple listing them i find sum of them
# Return true if perfect, return false if it isn't
# Get input from user
# Start while loop if number greater or equal to 1
# Call function in for loop, if true add it to tuple
# Get new input, restart while loop if greater or equal to one again

def findDivisors(num1):
    """Finds the common divisors of num1 
        Adds each of them to sum
        returns true if perfect
        returns false if not"""

    divisors = 0
    for i in range(1, num1):
        if num1 % i == 0:
            divisors += i
    if num1 == divisors:
        return True
    else:
        return False

num = int(input("Please enter a positive number to find perfect divisors: "))
while num >= 1:
    perfect = ()
    for i in range(1, num + 1):
        if findDivisors(i) == True:
            perfect += (i,)
    print(perfect)
    num = int(input("Please enter a positive number to find perfect divisors: "))
print("Finished!")

    


