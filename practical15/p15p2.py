# Create function
# Get input from user
# Start while loop for number >= 1
# print funct(x), each time, then blank line at end
# Get new input
# If number not >= 1 is entered, exit while loop

def funct(x):
    if x == 1:
        return 1
    else:
        # print("x is now", x)
        return (funct(x - 1) + 2 ** (x - 1))

num = int(input("Please enter a number greater than or equal to one: "))
while  num >= 1:
    for i in range(num):
        print(funct(i + 1), ", ", end="")
    print()
    num = int(input("Please enter a number greater than or equal to one: "))
print("Finished!")
exit()