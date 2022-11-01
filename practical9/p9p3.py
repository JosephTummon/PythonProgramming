# Get number
# Start for loop up to num + 1
# multiply by i each time 
# Print answer

num = int(input("Please enter a positive integer: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(num, "factorial is", fact)