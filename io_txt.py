import glob
import os

import cv2
import numpy as np
from pdf2jpg import pdf2jpg
from PIL import Image

from config import CFG, LOG

Image.MAX_IMAGE_PIXELS = None

# read image texts from different types (pdf, jpg, png, tif)
# pdf2jpg lib is used instead of pdf2image because in some cases pdf2image could generate undefined symbols 
# while converting pdf into images see https://github.com/Belval/pdf2image/issues/48

def read_file(file_path):
    images = []
    if '.pdf' in file_path or '.PDF' in file_path:
        file_dir_lst = file_path.split('/')
        file_dir = ''
        for i in file_dir_lst[:-1]:
            file_dir += (i + '/')
        # pdf2jpg is in java with python wrapper using os requests it is not possible to return images
        # so the extracted images from the java will be saved in a directory then read in python
        # this is time consuming but it handle the cases where pdf2image failed.
        pdf2jpg.convert_pdf2jpg(file_path, file_dir)
        i = 0
        while os.path.isfile(file_path + '_dir/' + str(i) + '_' + file_dir_lst[-1] + '.jpg'):
            img = cv2.imread(file_path + '_dir/' + str(i) + '_' + file_dir_lst[-1] + '.jpg')
            images.append(img)
            i += 1
        os.system('rm -r \'' +  file_path + '_dir/\'')
    else:
        try:
            img = cv2.imread(file_path)
            images.append(img)
        except:
            LOG.logger.info('Invalid Input Type')
    for i in range(len(images)):
        if len(np.array(images[i]).shape) == 2:
            images[i] = gray = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    return images

# write the resulted text in a file
def write_file(file_path, texts):
    output = open(file_path, 'w')
    for txt in texts:
        output.write(txt)
    output.close()
