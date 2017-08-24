import send2trash

potatoFile = open('potato.txt', 'a') #Creates the file
potatoFile.write('Potato is a vegetable.')

potatoFile.close()
send2trash.send2trash('potato.txt')

'''
you should always use the send2trash.send2trash() function to delete files and folders.
But while sending files to the recycle bin lets you recover them later, it will not free
up disk space like permanently deleting them does. If you want your program to free up
disk space, use the os and shutil functions for deleting files and folders. Note that
the send2trash() function can only send files to the recycle bin; it cannot pull files out of it.
'''
