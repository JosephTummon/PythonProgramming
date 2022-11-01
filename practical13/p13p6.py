# Using recursive function lecture 15
# Inserting print statement at start
# Inserting print statement before if != 1, b ecause 1 isn't multiplied by 0multiplication
# Inseting print statement after 0, to show it is ultiplied by 1
def fact(x):
    print("x is now:", x)
    if x == 0:
        print("Since x is 0, we multiply by 1, because 0! = 1")
        return 1
    else:
        if x != 1:
            print("In this step", x, "is multiplied by ", x - 1)
        return x * fact(x- 1)

num = int(input("Please enter a non-negative integer: "))
if num >= 0:
    print("The factorial of", num, "is", fact(num))
else:
    print("ERROR: Please enter a non-negative number.")