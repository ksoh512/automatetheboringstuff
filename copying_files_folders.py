import shutil, os

os.chdir('C:\\')

''' COPY FILES '''
shutil.copy('C:\\spam.txt', 'C:\\Users\\koh\\Documents\\codes\\automattheboringstuff')

shutil.copy('C:\\eggs.txt', 'C:\\Users\\koh\\Documents\\codes\\automattheboringstuff')


'''COPY FOLDERS AND FILES CONTAINED IN IT'''
shutil.copytree('C:\\delicious', 'C:\\Users\\koh\\Documents\\codes\\automattheboringstuff')
