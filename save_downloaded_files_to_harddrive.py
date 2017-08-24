import requests

#call requests.get() to download the file
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

#Call open() with 'wb' to create a new file in write binary mode
playFile = open('RomeoAndJuliet.txt', 'wb')

#Loop over the Response object's iter_content() method
#Call write() on each iteration to write the content to the file
for chunk in res.iter_content(100000):
    playFile.write(chunk)
    print('File has been written!')
#Call close() to close the file.
playFile.close()
