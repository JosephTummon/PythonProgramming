# Set counter and sum to 0
# Start while loop for counter <= 10000
# Check if mutiple of 5 or 3
# If multiple add on to sum, then add one to counter
# Else add one to counter
# Print sum
counter = 0
sum = 0

while counter <= 10000:
    if counter % 3 == 0:
        sum += counter
        counter += 1
    elif counter % 5 == 0:
        sum += counter
        counter += 1
    else:
        counter += 1
print(sum)