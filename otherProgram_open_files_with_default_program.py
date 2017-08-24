fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')

fileObj.close()

import subprocess

subprocess.Popen(['start', 'hello.txt'], shell=True)

'''
Here we write Hello world! to a new hello.txt file. Then we call Popen()
passing it a list containing the program name (in this example, 'start'
for Windows) and the filename. We also pass the shell=True keyword argument
which is needed only on Windows. The operating system knows all of the file
associations and can figure out that it should launch, say, Notepad.exe to
handle the hello.txt file.
'''
