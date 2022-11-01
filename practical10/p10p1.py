# Get integer from user
# Set check to 1
# Go through i in range number + 1
# if i^2 = num, it is square also change value of check
# After loop if check unchanged, print is not perfect square

num = int(input("Please enter a positive integer: "))
while num >= 0:
    check = 1
    for i in range(num + 1):
        if i ** 2 == num:
            print("The square root of", num, "is", i)
            check = 2
            num = int(input("Please enter a positive integer: "))
    if check == 1:
        print("This number is not a perfect square.")
        num = int(input("Please enter a positive integer: "))
print("Finished!")