#Writing the following string
##That is Alice's cat.
spam = "That is Alice's cat."
print(spam)
spam = 'That is Alice\'s cat.'
print(spam)

#Escape character
# \' : single quote
# \" : double quote
# \t : tab
# \n : newline (line break)
# \\ : backslash

print("Hello there! \nHow are you? \nI\'m doing fine.")

#raw string. Because this is a raw string, python considers
#the backslash as part of the string and not as the start of an escape character
print(r'That is Carol\'s cat.')
