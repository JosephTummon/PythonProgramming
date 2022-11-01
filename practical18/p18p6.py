# Check input file is there
import os
filename = 'read.txt'
if not os.path.isfile(filename):
    print("Problem finding file to read from")
else:
    fh1 = open(filename, 'r')
    ecount = 0
    leftcount = 0
    rightcount = 0
    linecount = 0
    leftstringcount = 0
    rightstringcount = 0
    string = "<!-- and the string -->"
    length = len(string)


    for i in fh1:
        linecount += 1
        for j in range(len(i)):
            if i[j] == "e":
                ecount += 1
            if i[j] == "<":
                leftcount += 1
            if i[j] == ">":
                rightcount += 1
            if i[j: j + 4] == "<!--":
                leftstringcount += 1
            if i[j: j + 3] == "-->":
                rightstringcount += 1
    fh1.close

writefile = "results.txt"
if not os.path.isfile(writefile):
    print("Problem finding file to write to") 
else:  
    fh2 = open(writefile, 'w')

    string1 = ("Number of lowercase e: ")
    string2 = ("Number of right brackets: ")
    string3 = ("Number of left brackets: ")
    string4 = ("Number of lines: ")
    string5 = ("Number of string <!--: ")
    string6 = ("Number of the string -->: ")
    fh2.write(string1)
    fh2.write(str(ecount))
    fh2.write("\n")
    fh2.write(string2)
    fh2.write(str(leftcount))
    fh2.write("\n")
    fh2.write(string3)
    fh2.write(str(rightcount))
    fh2.write("\n")
    fh2.write(string4)
    fh2.write(str(linecount))
    fh2.write("\n")
    fh2.write(string5)
    fh2.write(str(leftstringcount))
    fh2.write("\n")
    fh2.write(string6)
    fh2.write(str(rightstringcount))
    fh2.write("\n")

    fh2.close
