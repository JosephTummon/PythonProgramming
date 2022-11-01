# Get input from user
# Set counters to 0
# Create for loop going through string
# Check 3 letters at a time, if string is cat or dog increase counters
# Print counters

string = input("Please enter some text: ")
cat_count = 0
dog_count = 0
for i in range(len(string) - 2):
    if string[i: i + 3] == "cat":
        cat_count += 1
    if string[i: i + 3] == "dog":
        dog_count += 1
print("Cat appears", cat_count, "times.")
print("Dog appears", dog_count, "times.")