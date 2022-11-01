# Get number for user
# Start while loop for non-zero number
# Set check to 0
# start for loop to check if i ** 3 is equal to the number
# if it is change check value and print message
# if check is still 0, not a perfect cube
# get new input
# use same method for negative, just use abs() to make num positive
# careful to print out num and -i, both values should be negative
# If while loop exited, means 0 was entered, finish program

num = int(input("Please enter a non-zero integer: "))
while num != 0:
    check = 0
    if num > 0:
        for i in range(num + 1):
            if i ** 3 == num:
                print("The cubed root of", num, "is", i)
                check = 1
        if check == 0:
            print("This is not a perfect cube")
        num = int(input("Please enter a non-zero integer: "))

    # Negative number check
    if num < 0:
        neg = abs(num)
        for i in range(neg + 1):
            if i ** 3 == neg:
                print("The cubed root of", num, "is", -i)
                check = 1
        if check == 0:
            print("This is not a perfect cube")
        num = int(input("Please enter a non-zero integer: "))
print("Finished!")
exit()