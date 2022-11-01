# Create function that converts strings to chars
# Turn to lowercase and strip all non letter characters
#
# Go through string now and check if palindrome
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
            Recursive function."""
            if len(s) <= 1:
                # A palindrome of length 0 or 1 is a palindrome
                return True
            else:
                # Compare the first and the last letters and check the remainder
                # of the string
                return s[0] == s[-1] and isPal(s[1:-1])
            
    return isPal(toChars(s))


str = input("Enter a string (empty string to exit): ")
while str != '':
    if isPalindrome(str):
        print(str, "is a palindrome")
    else:
        print(str, "is not a palindrome")
    str = input("Enter a string (empty string to exit): ")
print("Finished!")
