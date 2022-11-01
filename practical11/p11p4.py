# Get integer from user
# Calulate n! factorial, 2n! and (n +1)!
# Sub into formula 
# Print result

num = int(input("Please enter an integer to calcualte Catalan number: "))

n_fact = 1
for i in range(1, num + 1):
    n_fact *= i
#print(n_fact)

twon_fact = 1
for i in range(1, (2 * num) + 1):
    twon_fact *= i
#print(twon_fact)

nplus_fact = 1
for i in range(1,num + 2):
    nplus_fact *= i
#print(nplus_fact)

catalan = twon_fact / (nplus_fact * n_fact)
print("The", num, "Catalan number is:", catalan)

