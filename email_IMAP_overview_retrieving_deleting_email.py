'''
the Internet Message Access Protocol (IMAP) specifies how to communicate with an email provider’s
server to retrieve emails sent to your email address.

The imapclient module downloads emails from an IMAP server in a rather complicated format.
Most likely, you’ll want to convert them from this format into simple string values.

The pyzmail module does the hard job of parsing these email messages for you.
'''

import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')

imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE 05-Jul-2014'])
print(UIDS)

rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
message.get_subject()

message.get_addresses('from')

message.get_addresses('to')

message.get_addresses('cc')

message.get_addresses('bcc')

message.text_part != None

message.text_part.get_payload().decode(message.textpart.charset)

message.html_part != None

message.html_part.get_payload().decode(message.html_part.charset)


imapObj.logout()

# Email Providers and Their IMAP Servers

# Gmail - imap.gmail.com
# Outlook.com/Hotmail.com - imap-mail.outlook.com
# Yahoo Mail - imap.mail.yahoo.com
# AT&T - imap.mail.att.net
# Comcast -  imap.comcast.net
# Verizon - incoming.verizon.net
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''
# CONNECTING TO AN IMAP SERVER
Once you have the domain name of the IMAP server, call the imapclient.IMAPClient() function
to create an IMAPClient object. Most email providers require SSL encryption, so pass the
ssl=True keyword argument.
'''
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

'''
Warning

Remember, never write a password directly into your code! Instead, design your program
to accept the password returned from input().

If the IMAP server rejects this username/password combination, Python will raise an
imaplib.error exception. For Gmail accounts, you may need to use an application-specific password;
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
# SEARCHING FOR EMAIL
Once you’re logged on, actually retrieving an email that you’re interested in is a two-step process.
First, you must select a folder you want to search through.
Then, you must call the IMAPClient object’s search() method, passing in a string of IMAP search keywords.
'''
'''
    # SELECTING a folder
        Almost every account has an INBOX folder by default, but you can also get a list of folders by calling
        the IMAPClient object’s list_folders() method. This returns a list of tuples. Each tuple contains
        information about a single folder.
        '''
        import pprint
        pprint.pprint(imapObj.list_folders())

        '''
        The three values in each of the tuples—for example, (('\\HasNoChildren',), '/', 'INBOX')—are as follows:

        A tuple of the folder’s flags. (Exactly what these flags represent is beyond the scope of this book,
        and you can safely ignore this field.)

        The delimiter used in the name string to separate parent folders and subfolders.

        The full name of the folder.

        To select a folder to search through, pass the folder’s name as a string into the IMAPClient object’s select_folder() method.
        '''

        imapObj.select_folder('INBOX', readonly=True)

        '''
        The readonly=True keyword argument prevents you from accidentally making changes or deletions to any of
        the emails in this folder during the subsequent method calls. Unless you want to delete emails, it’s a
        good idea to always set readonly to True.
        '''
'''
    # PERFORMING THE SEARCH
        With a folder selected, you can now search for emails with the IMAPClient object’s search() method.
        The argument to search() is a list of strings, each formatted to the IMAP’s search keys.
'''

'''
        'ALL' - Returns all messages in the folder. You may run in to imaplib size limits if you request all the messages in a large folder. See Size Limits.
        'BEFORE date', 'ON date', 'SINCE date' - These three search keys return, respectively, messages that were received by the IMAP server before, on, or after the given date. The date must be formatted like 05-Jul-2015. Also, while 'SINCE 05-Jul-2015' will match messages on and after July 5, 'BEFORE 05-Jul-2015' will match only messages before July 5 but not on July 5 itself.
        'SUBJECT string', 'BODY string', 'TEXT string' - Returns messages where string is found in the subject, body, or either, respectively. If string has spaces in it, then enclose it with double quotes: 'TEXT "search with spaces"'.
        'FROM string', 'TO string', 'CC string', 'BCC string' - Returns all messages where string is found in the “from” emailaddress, “to” addresses, “cc” (carbon copy) addresses, or “bcc” (blind carbon copy) addresses, respectively. If there are multiple email addresses in string, then separate them with spaces and enclose them all with double quotes: 'CC "firstcc@example.com secondcc@example.com"'.
        'SEEN', 'UNSEEN' - Returns all messages with and without the \Seen flag, respectively. An email obtains the \Seen flag if it has been accessed with a fetch() method call (described later) or if it is clicked when you’re checking your email in an email program or web browser. It’s more common to say the email has been “read” rather than “seen,” but they mean the same thing.
        'ANSWERED', 'UNANSWERED' - Returns all messages with and without the \Answered flag, respectively. A message obtains the \Answered flag when it is replied to.
        'DELETED', 'UNDELETED' - Returns all messages with and without the \Deleted flag, respectively. Email messages deleted with the delete_messages() method are given the \Deleted flag but are not permanently deleted until the expunge() method is called (see Deleting Emails). Note that some email providers, such as Gmail, automatically expunge emails.
        'DRAFT', 'UNDRAFT' - Returns all messages with and without the \Draft flag, respectively. Draft messages are usually kept in a separate Drafts folder rather than in the INBOX folder.
        'FLAGGED', 'UNFLAGGED' - Returns all messages with and without the \Flagged flag, respectively. This flag is usually used to mark email messages as “Important” or “Urgent.”
        'LARGER N', 'SMALLER N' - Returns all messages larger or smaller than N bytes, respectively.
        'NOT search-key' - Returns the messages that search-key would not have returned.
        'OR search-key1 search-key2' - Returns the messages that match either the first or second search-key.
'''

        #EXAMPLE
        imapObj.search(['ALL']) - Returns every message in the currently selected folder
        imapObj.search(['ON 05-Jul-2015']) - Returns every message sent on July 5, 2015
        imapObj.search(['SINCE 01-Jan-2015', 'BEFORE 01-Feb-2015', 'UNSEEN']) - Returns every message sent in January 2015
            that is unread. (Note that this means on and after January 1 and up to but not including February 1.)
        imapObj.search(['SINCE 01-Jan-2015', 'FROM alice@example.com']). Returns every message from alice@example.com sent since the start of 2015.
        imapObj.search(['SINCE 01-Jan-2015', 'NOT FROM alice@example.com']). Returns every message sent from everyone except
            alice@example.com since the start of 2015.
        imapObj.search(['OR FROM alice@example.com FROM bob@example.com']). Returns every message ever sent from alice@example.com
            or bob@example.com.
        imapObj.search(['FROM alice@example.com', 'FROM bob@example.com']). Trick example! This search will never return any
            messages, because messages must match all search keywords. Since there can be only one “from” address, it is impossible
            for a message to be from both alice@example.com and bob@example.com.

'''
'''
        The search() method doesn’t return the emails themselves but rather unique IDs (UIDs) for the emails, as integer values.
        You can then pass these UIDs to the fetch() method to obtain the email content.
'''
        UIDs = imapObj.search(['SINCE 05-Jul-2015'])
        print(UIDs)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
    # SIZE LIMITS
        If your search matches a large number of email messages, Python might raise an exception that says imaplib.error:
        got more than 10000 bytes. When this happens, you will have to disconnect and reconnect to the IMAP server and try again.
        Unfortunately, the default size limit is often too small. You can change this limit from 10,000 bytes to 10,000,000 bytes
        by running this code:
'''
        import imaplib

        imaplib._MAXLINE = 10000000

'''
        This should prevent this error message from coming up again. You may want to make these two lines part of every IMAP program
        you write.
'''
'''
    # Using Imapclient’s Gmail_Search( ) Method
         you can use Gmail’s more sophisticated search engine. Gmail does a good job of matching closely related words (for example,
         a search for driving will also match drive and drove) and sorting the search results by most significant matches. You can
         also use Gmail’s advanced search operators (see http://nostarch.com/automatestuff/ for more information). If you are logging
         in to a Gmail account, pass the search terms to the gmail_search() method instead of the search() method
'''
        UIDs = imapObj.gmail_search('meaning of life')
        print(UIDs)

'''
    # FETCHING AN EMAIL AND MARKING IT AS READ
        Once you have a list of UIDs, you can call the IMAPClient object’s fetch() method to get the actual email content.
        The list of UIDs will be fetch()’s first argument. The second argument should be the list ['BODY[]'], which tells
        fetch() to download all the body content for the emails specified in your UID list.
'''
        rawMessages = imapObj.fetch(UIDs, ['BODY[]'])

        import pprint

        pprint.pprint(rawMessages)
