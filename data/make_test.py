import os
from os import listdir
import random
import shutil

class_num = 50

def get_files_by_class(class_id):
    return listdir('train/{}'.format(class_id))

def get_sample_by_class(class_id, sample_frac):
    class_files = get_files_by_class(class_id)
    sample_size = int(sample_frac * len(class_files))
    sample_ids = [random.randint(0, len(class_files) - 1) for i in range(sample_size)]
    sample_files = list(map(lambda file_id: class_files[file_id], sample_ids))

    return sample_files

def update_art_validate(validate_frac=0.3):
    if os.path.exists("art_validate"):
        shutil.rmtree("art_validate")

    os.mkdir('art_validate')
    for class_id in range(class_num):
        os.mkdir('art_validate/{}'.format(class_id))
        for file_to_art_validate in get_sample_by_class(class_id, validate_frac):
            shutil.copyfile('train/{0}/{1}'.format(class_id, file_to_art_validate),
                            'art_validate/{0}/{1}'.format(class_id, file_to_art_validate)) 
#  print(get_sample_by_class(0, 0.3))

if __name__ == '__main__':
    update_art_validate()
