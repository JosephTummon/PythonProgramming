# Get input from user
# Create function
# Only asked to create isPal so presuming all lowercase and no spaces
# set check to 0
# Go through half of string and check if mathces last half
# Change check if it doesn't match
# Retrun True for Palindrome, False if it isn't

string = input("Please enter a string and i will check if it is a Palindrom: ")

def isPal(s):
    check = 0
    for i in range(int(len(s) / 2)):
        if s[i] == s[-(i + 1)]:
            check = 0
        else:
            check = 1
    if check == 0:
        return True
    else:
        return False
        
if isPal(string):
    print(string, "is a Palindrome")
else:
    print(string, "is not a Palindrome")