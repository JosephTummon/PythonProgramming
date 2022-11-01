#Taken from lecture 13, slide 16
#starts for loop for range
# then start seconds loop going uo to whichever number we are on
# if the number has any factors it prints it out lowest one then breaks
# if it gets up to number and has no factors we print that it is a prime

for number in range(2, 20):
    for i in range(2, number):
        if number % i == 0:
            print(number, "equals", i, "*", number//i)
            break
    else:
        # loop fell through without finding a factor
        print(number, "is a prime number")
print("Finished!")
