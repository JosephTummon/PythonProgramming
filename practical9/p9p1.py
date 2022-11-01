# Get number from user
# Set counter and sum to 0
# While counter is less than or equal to num enter while loop
# Add counter to sum and add one to counter
# Print result

num = int(input("Please enter a positive integer: "))
counter = 0
sum = 0

while counter <= num:
    sum += counter
    counter += 1
print(sum)
exit()