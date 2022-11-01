# Create function
# Go through entire string
# Set count to 0
# Check string in slices of first two letters and last letter
# Also make sure fourth letter is letter in alphabet
# Add to count if it satisfies the rules 
# Print answer
def code():
    """Checks how many times "code" appears in a string
    but theird character can be any lettr in alphabet and be upper or lowercase"""
    string = input("Please enter a string: ")
    count = 0
    for i in range(len(string - 3)):
        if string[i:i+2] == "co" and string[i+3] == "e" and string[i+2].lower() in "abcdefghijklmnopqrstuvwxyz":
            count +=1 
    print("'Code' appears", count, "times.")
code()