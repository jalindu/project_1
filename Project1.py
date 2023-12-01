import re
'''
# Project 1: Description:Website Sign Up. In this project, you will write a python program that prompts a user to sign up for a website. The user must come up with a username and password, then log in using the username and password.
There are requirements for both the username and password. If either one does not meet the requirements, print an appropriate error message and ask the user for a new username and password.
If they are both valid, store them as variables. Then ask the user to log in using the username and password they chose.

#2: Username Requirements - inform the user of these requirements: The username must:
Follow the python conventions for a variable name. It must start with a lowercase letter, and only contain letters, numbers, and underscores
Not be in a list of taken usernames. The list will be given to you
If the username does not meet the requirements, print either "Invalid username" or "Username taken" based on the context, and continue looping.

#3: Password Requirements - Inform the user of these requirements. The Password must be:
. At least 8 characters long
. Contains at least one uppercase letter
. Contains at least one lowercase letter
. Contains at least one digit
. Contains at least one of these characters: !, ?, @, #, $, ^, &, *, _,-
. Does not contain any spaces
If the password does not meet the requirements, print the message "Invalid password" and continue looping.

4: Logging In: Once the user has created a username and password, print "Sign up successful". Now prompt them to log in. Ask them to enter their username and password. If either one does not match, print "Incorrect username or password" and continue looping. Otherwise print "Login successful" and end the program.

'''
# Initializing all variables
username, password, entered_username, entered_password, register_username, register_password, username_login, password_login = '', '', '', '', '', '', '', ''

# Appropriate messages to print for user guidance
message_list = ['Invalid Username', 'Username Taken', 'Invalid Password','Signup Successful', 'Login Successful', 'Incorrect username or password']

# Prompt user to enter a chosen username up on website

while True:
    entered_username = input("Please enter your username: ")# Get username input
    entered_password = input("Please enter your password: ") # Get password input

# Begin username testing username for whether it is uppercase, since only lowercase should be allowed

    test_uppercase = entered_username[0].isupper()
    if test_uppercase:
        print(message_list[0])
        continue
# Test username allowed characters to complete registration
    register_username = bool(re.match("^[A-Za-z0-9_]*$", entered_username))
    if not register_username:
        print(message_list[0])
        continue

# List of taken usernames
    taken_usernames = ['admin', 'admin123','root']
    usernames_taken_test = entered_username in taken_usernames
    if usernames_taken_test:
        print(message_list[1])
        continue

# Password Length Test

    pw_length_test = len(entered_password) >= 8
    if not pw_length_test:
        print(message_list[2])
        continue
# Test password registration
    register_password = bool(re.match("^[A-Za-z0-9_!?@#$^&*_-]*$", entered_password))
    if register_password:
        print(message_list[3])
        

# Ensuring Registration
    username_registration = entered_username
    password_registration = entered_password
    print(message_list[3])
    

# Login to Website
    username_login = input("Username: Please enter your username to login: ")
    password_login = input("Password: Please enter your password to login: ")
    if username_login == username_registration and password_login == password_registration:
        print(message_list[4])
        break
    else:
        print(message_list[4])