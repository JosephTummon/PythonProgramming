larger_rate = 0.135
smaller_rate = 0.23

start_amount = 222081.16

larger_amount = start_amount * 0.6
smaller_amount = start_amount * 0.4

larger_tax = larger_amount * larger_rate
smaller_tax = smaller_amount * smaller_rate
total_tax = larger_tax + smaller_tax

total_amount = round((start_amount + total_tax), 2)
print("Total amount after tax is: €" , total_amount, sep="")

