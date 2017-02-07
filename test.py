import os
import shutil
import cv2
import numpy as np
import subprocess
import tempfile
import shutil


'''class CVLineDetection(object):
def __init__(self, image01Path01):
    pass'''
def listFiles(path, extension1,extension2,newfolder):
    #return [f for f in os.listdir(path) if f.endswith(extension)]
    files=[]
    if (os.path.isdir(newfolder))== False:
        os.mkdir(newfolder)

        line_files=[]
        image_files=[]
        files = os.listdir(path)
        for file in files:
            if file.endswith(extension1):
                line_files.append(file)
            elif file.endswith(extension2):
                image_files.append(file)

        for i in range(len(line_files)):
            shutil.copy(path+line_files[i],newfolder)
            shutil.copy(path + image_files[i], newfolder)



#listFiles('/home/deepayan/codes_seg/set1/', 'lines.txt',".jpg","/home/deepayan/codes_seg/set2/")
def get_position_1(image_name,s):
#files = os.listdir(folder)
    print s
   # print image_name
    #path = '/home/deepayan/codes_seg/data/'
    #name = (os.path.basename(str(image_name)))
    if os.path.exists(image_name + '.lines.txt') == True:
        os.remove(image_name+'.lines.txt')
        print "hiiiiiiiii"
        subprocess.call('./j-layout ' + image_name+' '+'-psm'+' '+str(s), shell=True)
    else:
        print "hiiiiiiiii"
        subprocess.call('./j-layout ' + image_name + ' ' + '-psm' + ' ' + str(s), shell=True)
    file_name =image_name+'.lines.txt'

    #file_name = image_name +'.lines.txt'

    #print file_name
    data =[]

    if file_name.endswith('.lines.txt'):
        data= np.loadtxt(file_name)
    '''if blocks_file.endswith('.blocks.txt'):
        blocks_data = np.loadtxt(blocks_file)'''
    return (data)

def get_position(image_name):
#files = os.listdir(folder)
   # print image_name
    #path = '/home/deepayan/codes_seg/data/'
    #name = (os.path.basename(str(image_name)))
    if os.path.exists(image_name + '.lines.txt') == False:
        subprocess.call('./j-layout ' + image_name, shell=True)

    file_name =image_name+'.lines.txt'

    #file_name = image_name +'.lines.txt'

    #print file_name
    data =[]

    if file_name.endswith('.lines.txt'):
        data= np.loadtxt(file_name)
    '''if blocks_file.endswith('.blocks.txt'):
        blocks_data = np.loadtxt(blocks_file)'''
    return (data)
#get_position("/home/deepayan/codes_seg/set2/")
def show_skew(image_name):
    image = cv2.imread(image_name)
    path = os.path.dirname(image_name)
    print path

    #if os.path.exists(image_name+'.lines.txt') == False:

    pos = np.loadtxt(image_name+'.lines.txt')
    for i in range(len(pos)):
        #for j in range(4):
        x1 = int(pos[i,0])
        #print x1
        y1 = int(pos[i,1])
        x2 = int(x1+pos[i,2])
        y2 = int(y1+pos[i,3])
        #print x1,y1,x2,y2
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, str(i), (x1-50,y1+25), font, 1, (0, 255, 0), 2)
        cv2.rectangle(image,(x1,y1),(x2,y2),(255,0,0), 2)
    #cv2.imshow('image',cv2.resize(image,(700,1000)))
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #if image.shape[1]>1000:

    cv2.imwrite(path+"/skew_temp.jpg",image)

def show_image(image_name,s):
    image = cv2.imread(image_name)
    path = os.path.dirname(image_name)
    name = os.path.basename(image_name)
    # ... do stuff with dirpath

    print path
    if s == 0:
        (pos)=get_position(image_name)
        print s
    else:
        (pos) = get_position_1(image_name,s)

    print len(pos)
    for i in range(len(pos)):
        #for j in range(4):
        x1 = int(pos[i,0])
        #print x1
        y1 = int(pos[i,1])
        x2 = int(x1+pos[i,2])
        y2 = int(y1+pos[i,3])
        #print x1,y1,x2,y2
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, str(i), (x1-50,y1+25), font, 1, (0, 255, 0), 2)
        cv2.rectangle(image,(x1,y1),(x2,y2),(255,0,0), 2)
    cv2.imwrite(path+'/temp.jpg',image)

def show_blocks(image_name):
    image = cv2.imread(image_name)
    clone = image.copy()
    [h, w] = clone.shape[:2]
    # newimage_name = image_name.split(".tif")[0]+"jpg"
    # cv2.imwrite(newimage_name,image)
    # image = cv2.imread(newimage_name)
    (pos, blocks_pos) = get_position(image_name)
    # print blocks_pos
    for j in range(len(blocks_pos)):
        bx1 = int(blocks_pos[j,0])
        by1 = int(blocks_pos[j,1])
        bx2 = int(bx1+blocks_pos[j,2])
        if bx2>w:
             bx2=(w-5)

        by2 = int(by1+blocks_pos[j,3])
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(clone, str(j), (bx1 - 50, by1 + 25), font, 1, (0, 255, 0), 2)
        cv2.rectangle(clone,(bx1,by1),(bx2,by2),(0,0,255), 2)
        #image = cv2.resize(image,(500,800))
    cv2.imshow("lalala", cv2.resize(image,(500,700)))
    cv2.waitKey(0)
    #cv2.imshow('lala',image)
    #cv2.imwrite("/home/deepayan/codes_seg/books_postcleaning/Malayalam/temp.jpg", clone)









