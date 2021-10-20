import os
import random
import imghdr

path = '.'

valid_directories = []
images = []

for dirpath, dirnames, files in os.walk('.', topdown=False):
    for file_name in files:
        if (imghdr.what(dirpath + '/' + file_name)):
            valid_directories.append(dirpath)

path = random.choice(valid_directories)
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        if(imghdr.what(path + '/' + entry)):
            images.append(entry)

print(random.choice(images))
