#! python 2.7
# Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY



import shutil, os, re

#TODO: Create a regex that matches files with the American date format
datePattern = re.compile(r"""^(.*?)         # all text before the date
    ((0|1)?\d)-                             # one or two digits for the month
    ((0|1|2|3)?\d)-                         # one or two digits for the day
    ((19|20)\d\d)                           # four digits for the year
    (.*?)$                                  # all text after the date
    """, re.VERBOSE)                        # re.VERBOSE will allow whitespace and comments in the regex string to make it more readable.

'''
    ^(.*?) to match any text at the beginning of the filename that might come before the date.
'''
'''
    ((0|1)?\d) group matches the month. The first digit can be either 0 or 1, so the regex matches
    12 for December but also 02 for February. This digit is also optional so that the month can be 04 or 4 for April.
'''
'''
    ((0|1|2|3)?\d) and follows similar logic; 3, 03, and 31 are all valid numbers for days. (Yes, this regex will accept
    some invalid dates such as 4-31-2014, 2-29-2013, and 0-15-2014. Dates have a lot of thorny special cases that can
    be easy to miss. But for simplicity, the regex in this program works well enough.
'''
'''
    (.*?)$ part of the regex will match any text that comes after the date.
'''
#TODO: Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    #TODO: Skip files without a date.
    if mo == None:
        continue

    #TODO: Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    #TODO: Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    #TODO: Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    #TODO: Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename)    #uncomment after testing
