# Took program from practical
# Left everything the same for num = 0, 1 & 2
# In the else statement can take out a and b variable, and just keep using f_0 and f_1

num = int(input("How many ters would you like me to calculare: "))
f_0 = 0
f_1 = 1

if num <= 0:
    print("Please enter a number greater than 0")
if num == 1:
    print("Series is:", f_0)
elif num == 2:
    print("Series is:", f_0, ",", f_1)
else:
    print("Series is: ", f_0, ", ", f_1, sep="", end="")
    i = 2
    while i < num:
        fib = f_1 + f_0
        print(", ", fib,sep="", end="")
        f_0 = f_1
        f_1 = fib
        i += 1
print()
print("Finished!")