# Get input from user
# Start while loops which works when num > 0
# Check if divisible for each number by using %
# Print message if or if not divisible 
# Get new number which will restart loop if non-negative
# Print finished if while loop exited, which would be caused by a negative number

num = int(input("Please enter a non-negative integer: "))
while num >= 0:
    if num % 2 == 0:
        print(num, "is divisble by 2")
    else:
        print(num, "is not divisble by 2")
    if num % 3 == 0:
        print(num, "is divisble by 3")
    else:
        print(num, "is not divisble by 3")
    if num % 5 == 0:
        print(num, "is divisble by 5")
    else:
        print(num, "is not divisble by 5")
    if num % 7 == 0:
        print(num, "is divisble by 7")
    else:
        print(num, "is not divisble by 7")
    num = int(input("Please enter a non-negative integer: "))
print("Finished!")
exit()