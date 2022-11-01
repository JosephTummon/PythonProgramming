# Create function
# Get two inputs
# Multiply each digit by base to power of how many digits in it is in string 
# Also give values to abcdef, if they are used
# When i find value of each digit i add it on to the total of the new number
def changebase():
    """ Change from any base to base 10"""
    number = input("Please enter a number: ").lower()
    base = int(input("Please enter a base up to 16: "))
    new_number = 0
    length = len(number)
    for i in range(len(number)):
        if number[i] == "a":
            new_number += 10 * (base ** (length - i - 1))
        elif number[i] == "b":
            new_number += 11 * (base ** (length - i - 1))
        elif number[i] == "c":
            new_number += 12 * (base ** (length - i - 1))
        elif number[i] == "d":
            new_number += 13 * (base ** (length - i - 1))
        elif number[i] == "e":
            new_number += 14 * (base ** (length - i - 1))
        elif number[i] == "f":
            new_number += 15 * (base ** (length - i - 1))
        else:
            new_number += int(number[i]) * (base ** (length - i - 1))
    print(new_number)
changebase()
