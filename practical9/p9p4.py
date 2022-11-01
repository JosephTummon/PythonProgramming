# Get input
# Start while loop for number > 0
# Took my code from p9p3 for getting factorial
# After calculating ask for new number
# If while loop exited print finished and exit

num = int(input("Please enter a positive integer: "))
if num == 0:
    print("Please enter a positive number")

while num > 0:
    fact = 1
    count = 1
    while count <= num:
        fact *= count
        count += 1
    print(num, "factorial is", fact)
    num = int(input("Please enter a positive integer: "))
print("Finished!")
exit()