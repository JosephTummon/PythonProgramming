# Create function
# Get length of both strings 
# Make them both lowercase
# Check if either string at end of the other, return true if they are
# Else return false

def checkstrings(a, b):
    """Checks whether one string is at the end of the other"""
    length1 = len(a)
    length2 = len(b)
    a = a.lower()
    b = b.lower()
    if a[-length2:length1] == b:
        return True
    elif b[-length1:length2] == a:
        return True
    else:
        return False
string1 = input("Please enter first string: ")
string2 = input("Please enter second string: ")
print(checkstrings(string1, string2))