# Create function
# Get input from user
# Start while loop if number positive
# Go through for loop to print each fibonacci number
# Get new number 
# if while loop exited print new number

### Note 0 term in fibonacci is 0 from formula but question says it should print as many
### terms as entered. So i made it if 1 is entered it only prints 1 term instead of printing
### the 0th term and the 1st term.
def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 0
    elif x == 2:
        return 1
    elif x >= 3:
        return(fib(x - 1) + fib(x - 2))

num = int(input("Please enter a non-negative number: "))
while num >= 0:
    for i in range(num):
        print(fib(i + 1), ", ", end="")
    print()
    num = int(input("Please enter a non-negative number: "))
print("Finished!")
