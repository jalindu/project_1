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
username = ''
password = ''