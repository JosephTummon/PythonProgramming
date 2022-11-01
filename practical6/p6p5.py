# Ask user to create password
# Ask user to enter password 
# If correct -> Login
# If incorrect ask user to enter password three times
# Check if their three guesses are correct -> login
# If any gfuess incorrect -> denied

password = input("Please create a password: ")

guess = input("Please enter your password: ")

if guess == password:
    print("You have successfully logged in.")
else:
    print("Sorry, this password is wrong: ")
    print("Please enter your password three times")
    guess1 = input("Enter password: ")
    guess2 = input("Enter password: ")
    guess3 = input("Enter password: ")

    if guess1 == guess2 == guess3 == password:
        print("You have successfully logged in.")
    else:
        print("You have been denied access.")

exit()