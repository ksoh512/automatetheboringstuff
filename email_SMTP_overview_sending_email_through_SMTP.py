import smtplib

smtpObj = smtplib.SMTP('smtp.example.com', 587)

smtpObj.ehlo()

smtpObj.starttls()

smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')

smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So long. \nDear Alicec, so long and thanks for all the fish. \
\n Sincerely, Bob')

smtpObj.quit()


# Connecting to an SMTP Server

# Gmail - smtp.gmail.com

# outlook.com/Hotmail.com - smtp-mail.outlook.com

# Yahoo mail - smtp.mail.yahoo.com

# AT&T - smpt.mail.att.net (port 465)

# Comcast - smtp.comcast.net

# Verizon - smtp.verizon.net(port 465)


smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
print(type(smtpObj))
# if smptlib.SMTP() call is not successful, your SMTP server might not support TLS on port 587.
# In this case, you will need to create an SMTP object using smtplib.SMTP_SSL() and port 465 instead.

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)


# SENDING THE SMTP "HELLO" MESSAGE

smtpObj.ehlo()

'''
(250, b'mx.google.com at your service, [216.172.148.131]\nSIZE 35882577\
n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
If the first item in the returned tuple is the integer 250 (the code for “success” in SMTP), then the greeting succeeded.
'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''
If you are connecting to port 587 on the SMTP server (that is, you’re using TLS encryption),
you’ll need to call the starttls() method next. This required step enables encryption for your
connection. If you are connecting to port 465 (using SSL), then encryption is already set up,
and you should skip this step.
'''

smartObj.starttls()

'''
starttls() puts your SMTP connection in TLS mode. The 220 in the return value tells you that the server is ready.
'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Once your encrypted connection to the SMTP server is set up, you can log in with your username
(usually your email address) and email password by calling the login() method.
'''

smtpObj.login(' my_email_address@gmail.com', ' MY_SECRET_PASSWORD ')

'''
Gmail’s Application-Specific Passwords

Gmail has an additional security feature for Google accounts called application-specific passwords.
If you receive an Application-specific password required error message when your program tries to
log in, you will have to set up one of these passwords for your Python script.
Pass a string of your email address as the first argument and a string of your password as the
second argument. The 235 in the return value means authentication was successful. Python will raise
an smtplib.SMTPAuthenticationError exception for incorrect passwords.

'''
'''
Warning

Be careful about putting passwords in your source code. If anyone ever copies your program,
they’ll have access to your email account! It’s a good idea to call input() and have the user
type in the password. It may be inconvenient to have to enter a password each time you run your
program, but this approach will prevent you from leaving your password in an unencrypted file on
your computer where a hacker or laptop thief could easily get it.

'''

# SENDING AN EMAIL

smtpObj.sendmail(' my_email_address@gmail.com', ' recipient@example.com ',
'Subject: so long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')

'''
The sendmail() method requires three arguments.
    Your email address as a string (for the email’s “from” address)
    The recipient’s email address as a string or a list of strings for multiple recipients (for the “to” address)
    The email body as a string

The start of the email body string must begin with 'Subject: \n' for the subject line of the email.
The '\n' newline character separates the subject line from the main body of the email.

The return value from sendmail() is a dictionary. There will be one key-value pair in the dictionary
for each recipient for whom email delivery failed. An empty dictionary means all recipients were successfully sent the email.
'''

# DISCONNECTING FROM THE SMTP SERVER

smtpObj.quit()
'''
The 221 in the return value means the session is ending.
'''
