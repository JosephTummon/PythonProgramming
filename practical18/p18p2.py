# Create function
# Go through entire string
# Set count to 0
# Check string in slices of four, if slice is code add to counter
# Print answer
def code():
    """Checks how many times "code" appears in a string"""
    string = input("Please enter a string: ")
    count = 0
    for i in range(len(string - 3)):
        if string[i:i+4] == "code":
            count +=1 
    print("'Code' appears", count, "times.")
code()