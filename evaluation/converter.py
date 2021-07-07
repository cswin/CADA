import os
from PIL import Image
dir = '/home/charlietran/domain/AWC-master/data/trial_1/'
dir_2 = '/home/charlietran/domain/AWC-master/data/trial_1_bmp/'
files = os.listdir(dir)

for file in files:

   # img = Image.open(dir + file)
    img = Image.open(dir + file)
    filename, file_extension = os.path.splitext(file)
   # print(dir + filename)
    img.save( dir_2 + filename + '.bmp')
    #print(img)
    #img.save('/home/charlietran/domain/AWC-master/data/trial_1_bmp/', 'bmp')
    #

    #f#ile_out = filename + '.bmp'
    #img.save(file_out, '/home/charlietran/domain/AWC-master/data/trial_1_bmp/')
