import os
import shutil


''' os module will help delete a single file or a single empty folder with functions '''
#os.unlink(path)
#os.rmdir(path)

''' shutil module will help delete a folder and all of its contents '''
#shutil.rmtree(path)

for filename in os.listdir():
    if filename.endswith('.rxt'):
        os.unlink(filename)
        print('You deleted' + filename)
