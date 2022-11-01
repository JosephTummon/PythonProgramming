#Taken from lecture 13, slide 16
#starts for loop for range
# Set the check to 0
# then start seconds loop going uo to whichever number we are on
# if the number has any factors it prints it out and continues, without a break
# if it gets up to number and check hasn't changed it must be a prime
for number in range(2, 20):
    check = 0
    for i in range(2, number):
        if number % i == 0:
            print(number, "equals", i, "*", number//i)
            check += 1
    if check == 0:
        print(number, "is a prime number")
print("Finished!")
