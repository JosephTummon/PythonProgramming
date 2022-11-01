larger_rate = 0.135
smaller_rate = 0.23

while True:
    try:
        start_amount = float(input("Please enter starting amount: "))
    except ValueError:
        print("Please enter a number!")
        continue
    else:
        break
            


larger_amount = start_amount * 0.6
smaller_amount = start_amount * 0.4

larger_tax = larger_amount * larger_rate
smaller_tax = smaller_amount * smaller_rate
total_tax = larger_tax + smaller_tax

total_amount = round((start_amount + total_tax), 2)
print("The initial amount is: €" , start_amount, sep="")
print("The larger tax amount is: €", larger_tax)
print("The smaller tax amount is: €", smaller_tax)
print("The total tax is: €", total_tax)
print("Total amount after tax is: €" , total_amount, sep="")