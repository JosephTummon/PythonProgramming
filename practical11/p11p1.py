# Calculating the factorial of a number
# Program prompts the user for the number
# Prompt the user for a number
# If less than 0, print error
# If greater than 0, set fact and i to 1 so even zero and one will return one as fact
# go through while loop multiplying until you reach number
# Print answer

number = int(input("Please enter a number for which you wish to calculate the factorial: "))
if number < 0:
    print("Error: Number entered was less than 0.")
    exit()
else:
    fact = 1
    i = 1
    while i <= number:
        fact *= i
        i += 1
print("Factorial of", number, "is", fact)
print("Finished")
