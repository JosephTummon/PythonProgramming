# Set password as dogb
# Create for loop for amount of guesses (3)
# Ask them to guess password
# If correct -> login -> exit
# If not guessed correctly after for loop, print denied access

password = "dog"

for i in range(3):
    guess = input("Please enter password: ")
    if guess == password:
        print("You have successfully logged in")
        exit()
    else:
        print("Incorrect password you have", 2 - i, "guesses remaining.")
print("You have been denied access")

exit()