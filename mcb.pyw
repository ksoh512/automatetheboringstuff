#! python 2.7
# mcb - multi clip board
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#TODO: Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':    #Is there 3 arguments and is the second argument "save"?
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:                                    #Is there 2 arguments?

    #TODO: List keywords and load content
    if sys.argv[1].lower() == 'list':                       #Is the second argument "list"?
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
