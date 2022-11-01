# Create function
# Get input from user
# Make sure base if less than 2
# Create empty list
# If number is bigger than base, find remainder and add to new_number
# If remainder is greater than 9, turn it into corresponding letter
# Go through until number is smaller than base, then just add number
# Print it without "," and brackets

def changeBase():
    """Function that changes from base ten to whatever base you'd like"""
    a = int(input("Please enter a number you would like to change: "))
    b = int(input("Please enter new base you would like to use: "))

    if b < 2:
        print("Please enter base greater than 1")
        exit()
    new_number = []
    while a > b:
        r = a % b
        if r > 9:
            numbers = [10, 11, 12, 13, 14, 15]
            letters = ["A", "B", "C", "D", "E", "F"]
            for i in range(len(numbers)):
                if numbers[i] == r:
                    r = letters[i]
        new_number.insert(0, r)
        a = a // b
    if a < b:
        new_number.insert(0, a)
    for i in new_number:
        print(i, end="")
    print()
changeBase()