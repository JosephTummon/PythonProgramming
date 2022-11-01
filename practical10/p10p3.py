# Get text from user
# Start while loop when string is not empty
# Set count for each to 0, don't label i i, use something different
# Start for loop, going through each letter of string
# If letter is there, add to count
# Print all the counts and total
# Ask for new input, if it isn't empty should start while loop again

text = input("Please enter some text: ")

while text != "":
    a = 0
    e = 0
    icount = 0
    o = 0
    u = 0
    for i in range(len(text)):
        if text[i] == "a" or text[i] == "A":
            a += 1
        elif text[i] == "e" or text[i] == "E":
            e += 1
        elif text[i] == "i" or text[i] == "I":
            icount += 1
        elif text[i] == "o" or text[i] == "O":
            o += 1
        elif text[i] == "u" or text[i] == "U":
            u += 1
    total = a + icount + o + u + e
    print("The letter a appears", a, "times.")
    print("The letter e appears", e, "times.")
    print("The letter i appears", icount, "times.")
    print("The letter o appears", o, "times.")
    print("The letter u appears", u, "times.")
    print("There are", total, "vowels in total")
    text = input("Please enter some text: ")
print("Finished!")
exit()