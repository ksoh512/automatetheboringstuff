import os


#Backslash on Windows and Forward Slash on OS X and Linux
print(os.path.join('usr', 'bin', 'spam'))


myFiles = ['accounts.txt', 'details.csv', 'invite.docx']




for files in myFiles:
    print(os.path.join('C:\\Users\\koh', files))



#The Current Working Directory
print(os.getcwd())

os.chdir('C:\\Windows\\System32')
print(os.getcwd())
