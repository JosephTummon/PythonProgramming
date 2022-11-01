# This is algorithm from lecture notes from wikepedia 

#  Algorithm (from Wikipedia)
#  The following pseudocode determines whether a year is a leap
#  year or a common year in the Gregorian calendar:
#  if (year is not exactly divisible by 4) then (it is a common year)
#  else
#  if (year is not exactly divisible by 100) then (it is a leap year)
#  else
#  if (year is not exactly divisible by 400) then (it is a common year)
#  else (it is a leap year)

year = int(input("Please enter a year: "))

if year % 4 != 0:
    print("This is a common year")
elif year % 100 != 0:
    print("This is a leap year")
elif year % 400 != 0:
    print("This is a common year")
else:
    print("This is a leap year")