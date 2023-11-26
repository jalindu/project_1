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
unacceptable_usernames = ['administrator', 'admin', 'root', 'supervisor', 'sup123', 'jalindu']

# Acceptable characters in username input
acceptable_username_characters = '0123456789abcdefghijklmnopqrstuvwxyz_'

# Acceptable special characters in password input
acceptable_password_characters = '!?@#$^&*_-'

# Appropriate messages to print for user guidance
message_list = ['Sign up successful', 'Login successful', 'Username taken','Invalid username', 'Invalid password''Incorrect username or password']

# Prompt user to sign up on website

while True:
    entered_username = input("Please enter your username: ")
    entered_password = input("Please enter your password: ")

# Test username
if entered_username in unacceptable_usernames:
    print(message_list[3])
    continue
# Test password
if len(entered_password) >= 8:
elif:
return False




