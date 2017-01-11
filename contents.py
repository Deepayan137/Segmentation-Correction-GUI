import os
import glob
import pandas as pd
import numpy as np

def find(name, path):
    count=0
    files = glob.glob1(path, "*.jpg")
    #print files

    index= files.index(name)

    tifCounter = len(glob.glob1(path, "*.jpg"))

    return index,tifCounter-1




