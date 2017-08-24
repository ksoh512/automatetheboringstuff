while True:
    print('Enter your age: ')
    age = raw_input()
    if age.isdigit():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only)')
    password = raw_input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')


#In the first while loop, we ask the user for their age and store their
#input in age. If age is a valid (decimal) value, we break out of this
#first while loop and move on to the second, which asks for a password.
#Otherwise, we inform the user that they need to enter a number and again
#ask them to enter their age. In the second while loop, we ask for a password,
#store the user’s input in password, and break out of the loop if the input
#was alphanumeric. If it wasn’t, we’re not satisfied so we tell the user
#the password needs to be alphanumeric and again ask them to enter a password.
