# Get number from user
# Set some and counter to 0
# use while loop to mkae sure positive number being entered
# Use for loop for sum
# Print answer then get another input

num = int(input("Please enter a positive integer: "))
counter = 0
sum = 0

while num > 0:
    for i in range(num + 1):
        sum += i
    print(sum)
    sum = 0
    num = int(input("Please enter a positive integer: "))
print("Finished!")
exit()