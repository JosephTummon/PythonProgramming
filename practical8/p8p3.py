# Get input from user
# Set counter to 0
# Set up while loop for counter going up to 20
# Print the counter
# Then print number by counter
# New line then restart while loop

# I'm not sure if it was neccessary but attempted to actually print table too, bit messy

num = int(input("Please enter a non-negative integer: "))
counter = 0
print("|Times", num, "Table|")
while counter <= 20:
    if counter >= 10:
        print("|",counter , "|", end="")
    else:
        print("| ", counter , "|", end="")
    mod = counter * num
    multiple = mod
    x = 0
    while (mod // 10) > 0:
        x += 1
        mod = mod // 10
    y = 5 - x
    print(y * " ", multiple ,"|")
    counter += 1
