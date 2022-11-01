# Set counters for each range to 0
# Get input for number
# Enter while loop if number is positive
# if in range add one to counter and print message, get new input for number
# If loop exited print out counters in message so you can see how many numbers were in each range

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
num = int(input("Please enter a positive integer: "))
while num >= 0:
    if num == 0:
        print("Number is equal to 0")
        a += 1
        num = int(input("Please enter a positive integer: "))

    elif num > 0 and num <= 20:
        print("Number is greater than 0 and less than or equal to 20")
        b += 1  
        num = int(input("Please enter a positive integer: "))

    elif num > 20 and num <= 40:
        print("Number is greater than 20 and less than or equal to 40")
        c += 1
        num = int(input("Please enter a positive integer: "))

    elif num > 40 and num <= 60:
        print("Number is greater than 40 and less than or equal to 60")
        d += 1
        num = int(input("Please enter a positive integer: "))

    elif num > 60 and num <= 80:
        print("Number is greater than 60 and less than or equal to 80")
        e += 1
        num = int(input("Please enter a positive integer: "))

    elif num > 80 and num <= 100:
        print("Number is greater than 80 and less than or equal to 100")
        f += 1
        num = int(input("Please enter a positive integer: "))

    else:
        print("NUmber is greater than 100")
        g += 1
        num = int(input("Please enter a positive integer: "))

print("There are", a, "numbers equal to 0")
print("There are", b, "numbers greater than 0 and less than 20")
print("There are", c, "numbers greater than 20 and less than 40")
print("There are", d, "numbers greater than 40 and less than 60")
print("There are", e, "numbers greater than 60 and less than 80")
print("There are", f, "numbers greater than 80 and less than 100")
print("There are ", g, "numbers greater than 100")
print("Finished!!")
exit()
