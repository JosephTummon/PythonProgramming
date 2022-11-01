while True:
    try:
        euro_amount = float(input("Enter euro amount to be converted to pounds: "))
    except ValueError:
        print("Please enter a number!")
        continue
    else:
        break
rate = 0.87
pound_amount = round((rate * euro_amount), 2) #round to 2 decimal places
print("€", euro_amount, " is £", pound_amount, sep="")