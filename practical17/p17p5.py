# Create Palindrome function 
# Creat isChar function in isPalindrome that converts strings to chars
# Turn to lowercase and strip all non letter characters
# Create isPal also inside isPalindrome
# This starts withouter two then calls it for string without first and last letter
# When working in will return false if it finds not a palindrome.
def isPalindrome(s):
    """Checks whether the string s is a palindrome
    Assumes s is a str.
    Returns True if the letters in s form a palindrome;
    Returns False otherwise.
    Case and non-letters are ignored."""

    def toChars(s):
        s = s.lower()
        letterstring = ""
        for a in s:
            if a in "abcdefghijklmnopqrstuvwxyz":
                letterstring += a
        return letterstring

    def isPal(s):
            """Checks whether the string s is a palindrome
            Assumes that s is a str with only lowercase letters and no
            non-letters.
            Returns True if s is a palindrome;
            Returns False otherwise.
            Recursive function.
            Has print statements to trace it's operation"""
            print("isPal function called with argument", s)
            if len(s) <= 1:
                print("About to return true isPal from basecase")
                # A palindrome of length 0 or 1 is a palindrome
                return True
            else:
                # Compare the first and the last letters and check the remainder
                # of the string
                result = s[0] == s[-1] and isPal(s[1:-1])
                print("About to return result", result, "from isPal with argument", s)
                return result
            
    return isPal(toChars(s))


str = input("Enter a string (empty string to exit): ")
while str != '':
    if isPalindrome(str):
        print(str, "is a palindrome")
    else:
        print(str, "is not a palindrome")
    str = input("Enter a string (empty string to exit): ")
print("Finished!")
