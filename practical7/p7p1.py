# Read year
# if year greater than 0
#if year not greater than 0, say must be positive
    #check if (year mod 4 = 0 and year mod 100 = 0) or (year mod 400 = 0)
# else print year isn't leap


year = int(input("Please enter year: "))

if year < 0:
    print("Must be greater than 0!")
else:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("This is a leap year")
    else:
        print("This isn't a leap year")