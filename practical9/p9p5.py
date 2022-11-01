# Get options (n)
# Get allowed (k)
# Calculate factorials 
# Use formual 
# Print answer

## Assuming you can't have more toppings then there are possibilities

options = int(input("How many options are there for toppings: "))
allowed = int(input("How many toppings are allowed on a pizza: "))

# n!
n_fact = 1
for i in range(1, options + 1):
    n_fact *= i

# k!
k_fact = 1
for i in range(1, allowed + 1):
    k_fact *= i

# (n - k)!
dif = options - allowed
nk_fact = 1
for i in range(1, dif + 1):
    nk_fact *= i

answer = (n_fact / (k_fact * nk_fact))
print("Number of possible toppings:", answer)
