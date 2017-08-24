import zipfile, os

os.chdir('C:\\')        # move to the folder with example2.zipfile
exampleZip = zipfile.ZipFile('example2.zip')

exampleZip.extractall()
exampleZip.close()


exampleZip.extract('spam.txt')
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
exampleZip.close()
