# Get number from user 
# Set counter and multiplier to user
# Set up main while loop that keeps track or what each row is multiplied by
# Set up second while loop that will multiply out and print each row
# Print blank line, and add 1 to both multiplier and counter before restarting 
# Need to change spacing so works when numbers are >= 100

num = int(input("Please enter a positive integer: "))
counter = 1
multiplier = 1
while multiplier <= num:
    while counter <= num:
        x = counter * multiplier
        if x < 10:
            print(x, " ", end="")
        else:
            print(x, end=" ")
        counter += 1
    print()
    multiplier += 1
    counter = 1