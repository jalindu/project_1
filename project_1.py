import re
#1Project 1: Description:Website Sign Up. In this project, you will write a python program that prompts a user to sign up for a website. The user must come up with a username and password, then log in using the username and password.
# There are requirements for both the username and password. If either one does not meet the requirements, print an appropriate error message and ask the user for a new username and password.
# If they are both valid, store them as variables. Then ask the user to log in using the username and password they chose.

#2: Username Requirements - inform the user of these requirements: The username must:
#. Follow the python conventions for a variable name. It must start with a lowercase letter, and only contain letters, numbers, and underscores
#. Not be in a list of taken usernames. The list will be given to you
# If the username does not meet the requirements, print either "Invalid username" or "Username taken" based on the context, and continue looping.

#3: Password Requirements - Inform the user of these requirements. The Password must be:
#. At least 8 characters long
#. Contains at least one uppercase letter
#. Contains at least one lowercase letter
#. Contains at least one digit
#. Contains at least one of these characters: !, ?, @, #, $, ^, &, *, _,-
#. Does not contain any spaces
# If the password does not meet the requirements, print the message "Invalid password" and continue looping.

# 4: Logging In: Once the user has created a username and password, print "Sign up successful". Now prompt them to log in. Ask them to enter their username and password. If either one does not match, print "Incorrect username or password" and continue looping. Otherwise print "Login successful" and end the program.

# Initializing all variables
username, password, entered_username, entered_password = '', '', '', ''

# List of taken usernames
taken_usernames = ['admin', 'admin123','root']

# Acceptable characters in username input
username_characters = '0123456789abcdefghijklmnopqrstuvwxyz_'

# Acceptable special characters in password input
acceptable_password_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!?@#$^&*_-'

# Appropriate messages to print for user guidance
message_list = ['Sign up successful', 'Login successful', 'Username taken','Invalid username', 'Invalid password', 'Incorrect username or password']

# Prompt user to sign up on website

while True:
    entered_username = input("Please enter your username: ")# Get inputs
    print(entered_username)
    
    # Begin username testing to check for whether username is taken

    if entered_username not in taken_usernames:
        print(message_list[0])

    else:
        print(message_list[3])
        continue

    fail = False
    # Test for whether username contains acceptable characters
    for t in entered_username:
        if t not in username_characters:
            print(message_list[3])
            fail = True
            break
    if fail:
        continue
    print(message_list[0])
    break

# Begin password testing
while True:
    entered_password = input("Please enter your password: ")# Get inputs
    print(entered_password)

# Test for length of characters in entered password
    if len(entered_password) >= 8:
         print(entered_password)
    else:
        print(message_list[4])


 # Test for acceptable characters in password input
    fail = False
    # Test for whether username contains acceptable characters
    for t in entered_password:
        if t not in acceptable_password_characters:
            print(message_list[4])
            fail = True
            break
    if fail:
        continue
    print(message_list[0])
    break
