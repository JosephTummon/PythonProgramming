# Open file and create counts for everything
# Go through each line and charcater and check for everything we are looking for
# Add to count whenever something appears
# Print totals
# Check if each type of bracket is matching, print error is not 

fh1 = open('brackets.txt', 'r')
normalleft = 0
normalright = 0
angleleft = 0
angleright= 0
squareleft = 0
squareright = 0
fancyleft = 0
fancyright = 0
for i in fh1:
    for j in range(len(i)):
        if i[j] == "(":
            normalleft += 1
        if i[j] == ")":
            normalright += 1
        if i[j] == "<":
            angleleft += 1
        if i[j] == ">":
            angleright += 1
        if i[j] == "[":
            squareleft += 1
        if i[j] == "]":
            squareright += 1
        if i[j] == "{":
            fancyleft += 1
        if i[j] == "}":
            fancyright += 1
        
    
        
        
print("Normal left bracket appears", normalleft, "times")
print("Normal right bracket appears", normalright, "times")
print("Angle left bracket appears", angleleft, "times")
print("Angle right bracket appears", angleright, "times")
print("Square left bracket appears", squareleft, "times")
print("Square right bracket appears", squareright, "times")
print("Fancy left bracket appears", fancyleft, "times")
print("Fancy right bracket appears", fancyright, "times")
if normalleft != normalright:
    print("Normal brackets not balanced!!!")
if angleleft != angleright:
    print("Angular brackets not balanced!!!")
if squareleft != squareright:
    print("Square brackets not balanced!!!")
if fancyleft != fancyright:
    print("Fancy brackets not balanced!!!")
fh1.close