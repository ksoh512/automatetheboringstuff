import webbrowser, sys

if len(sys.argv) > 1:
    #Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    #TODO: Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)
