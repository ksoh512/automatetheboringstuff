#There are three steps to reading or writing files in python
#open()
#read(), write()
#close()

import os

helloFile = open('C:\\Users\\koh\\Documents\\codes\\automattheboringstuff\\hello.txt')

helloContent = helloFile.read()             #read the file
print(helloContent)

sonnetFile = open('sonnet29.txt')
print(sonnetFile.readlines())               #readlines from the file


baconFile = open('bacon.txt', 'w')
baconFile.write('Hello Bacon!\nThis is Kyu from the otherside!')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('\nBacon is not a vegetable.')

baconFile.close()
baconFile = open('bacon.txt')

content = baconFile.read()
baconFile.close()
print(content)
