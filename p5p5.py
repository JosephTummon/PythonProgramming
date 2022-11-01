city = input("Please enter the name of an Irish city: ")

connacht = ["Galway", "Sligo"]
ulster = ["Belfast", "Derry", "Lisburn"]
leinster = ["Dublin", "Kilkenny"]
munster = ["Cork", "Limerick", "Waterford"]

if city in connacht:
    print("You entered " + city + ". " + city + " is in Connacht")
elif city in ulster:
    print("You entered " + city + ". " + city + " is in Ulster")
elif city in leinster:
    print("You entered " + city + ". " + city + " is in Leinster")
elif city in munster:
    print("You entered " + city + ". " + city + " is in Munster")
else:
    print("Sorry, I didn’t recognise that name.")

