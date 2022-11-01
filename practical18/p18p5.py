from sqlalchemy import false


# Create function
# Set check to 0, 
# Create for loop going through function , check for xyz then check for .
# change check if satisifies condition
# Print function at end to see if working correctly

def xyz():
    """Checks whether "xyz" appears without ."""
    string = input("Please enter a string: ")
    check = 0
    for i in range(len(string)):
        if string[i: i+3] == "xyz":
            if string[i-1] != ".":
                check = 1
    if check == 0:
        return False
    else:
        return True
print(xyz())