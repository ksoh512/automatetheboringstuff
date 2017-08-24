import zipfile, os

os.chdir('C:\\') #move to the folder with example.zipfile

exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())

spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)

print(spamInfo.compress_size)

print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))

exampleZip.close()
