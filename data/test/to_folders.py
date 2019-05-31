import os
from os import listdir
import random
import shutil

class_num = 50

def get_files():
    return listdir('.')

def files_to_folders():
    files = get_files()
    
    for filename in files: 
        os.mkdir('folder_{}'.format(filename))
        
        shutil.copyfile(f'{filename}', f'folder_{filename}/{filename}')

if __name__ == '__main__':
    files_to_folders()
