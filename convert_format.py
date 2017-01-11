import cv2
import os
import subprocess
from PIL import Image
def convert(path):

    for dirname, dirnames, filenames in os.walk(path):

        #for subdirname in dirnames:

         #   for _, _, files in os.walk(os.path.join(dirname, subdirname)):
        for file in filenames:
            if file.endswith('.TIF'):
                filepath = (os.path.join(dirname, file))

                new_imageName = file.split(".")[0] + '.jpg'
                image = Image.open(filepath)
                #image = cv2.imread(filepath)
                image.save(path+new_imageName)




