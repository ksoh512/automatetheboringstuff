import pyperclip, re


# TODO: Create phone regex

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  #area code
    (\s|-|\.)?                          #separator
    (\d{3})                             #first 3 digits
    (\s|-|\.)                           #separator
    (\d{4})                             #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      #extension
)''', re.VERBOSE)


# TODO: Create email regex.

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                   #username
    @                                   #@ symbol
    [a-zA-Z0-9.-]+                      #domain names
    (\.[a-zA-Z]{2-4})                   #dot-something
)''', re.VERBOSE)

# TODO: Find matches in clipboard text.

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#As you can see at ❶, you’ll store the matches in a list variable named matches. It starts off as an empty list, and a couple for loops. For the email addresses, you append group 0 of each match ❸. For the matched phone numbers, you don’t want to just append group 0. While the program detects phone numbers in several formats, you want the phone number appended to be in a single, standard format. The phoneNum variable contains a string built from groups 1, 3, 5, and 8 of the matched text ❷. (These groups are the area code, first three digits, last four digits, and extension.)

# TODO: Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
