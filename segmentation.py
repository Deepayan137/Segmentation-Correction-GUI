import os
import sys
import subprocess
import cv2
import numpy as np
from editShapes import change,shift
c=0
state =0
def box(dir):
    files = os.listdir(dir)
    for file in files:
        path=dir+file
        subprocess.call('./j-layout '+path,shell=True)
'''for file in os.listdir("/home/deepayan/codes_seg/new_set2/"):
    if file.endswith(".jpg"):
        c+=1
        box('/home/deepayan/codes_seg/new_set2/'+file)
        print c'''
#box('/home/deepayan/codes_seg/data/new_set/')
def click_drag(tempFile,image_name,path):
   
    name = (os.path.basename(str(image_name)))
    file_name = path+ name + '.lines.txt'
    print file_name

    def draw_rect(event, x, y, flags, param):
        # grab references to the global variables
        global refPt, cropping

        # if the left mouse button was clickede, record the starting
        # (x, y) coordinates and indicate that cropping is being
        # performed
        if event == cv2.EVENT_LBUTTONDOWN:
            refPt = [(x, y)]


        # check to see if the left mouse button was released
        elif event == cv2.EVENT_LBUTTONUP:
            # record the ending (x, y) coordinates and indicate that                                                          qq
            # the cropping operation is finished
            refPt.append((x, y))


            # draw a rectangle around the region of interest
            cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
            cv2.imshow("image", image)
            #cv2.imwrite(image_name,image)

    image = cv2.imread(tempFile)


   # clone = image.copy()
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 500,800)
    cv2.setMouseCallback("image", draw_rect)
    #file_name = "/home/deepayan/codes_seg/set2/SiddhantaChandrika_Page_05.jpg.lines.txt"
    #clone = image.copy()
    # print file_name
    data = []


    data = np.loadtxt(file_name)

        #print data
    #textfile = open(image+'.lines.txt','a')

    while(1):
        cv2.imshow("image",image)
        k = cv2.waitKey(20) & 0xFF
        if k == ord('q'):
            break
        elif k == ord('a'):
            data =  np.append(data, np.array([[refPt[0][0],refPt[0][1],(refPt[1][0]-refPt[0][0]),(refPt[1][1]-refPt[0][1])]]), axis=0 )
            #print data
        elif k== ord('r'):
            image = clone.copy()

    data = data[data[:, 1].argsort()]
    cv2.destroyAllWindows()
    np.savetxt(file_name,data,delimiter=' ')


def findIndex(pts, file_name):
    data = np.loadtxt(file_name)
    pos = []
    x = pts[0][0]
    y = pts[0][1]
    w = pts[1][0] - pts[0][0]
    h = pts[1][1] - pts[0][1]
    for i in range(len(data)):
        npx = data[i][0]
        npy = data[i][1]
        npw = data[i][2]
        nph = data[i][3]
        if x < npx and y <= npy:
            if x+w > npx+npw and y+h > npy+nph:
                pos.append(i)

    return pos
def findIndex2(p,q, file_name):
    data = np.loadtxt(file_name)
    pos = 0
    x = p
    y = q
    print x,y
    for i in range(len(data)):
        npx = data[i][0]
        npy = data[i][1]
        npw = data[i][2]
        nph = data[i][3]
        if x>npx and y>npy:
            if x < npx+npw and y<npy+nph:
                pos=i
    return  pos
#click_drag("/home/deepayan/codes_seg/set2/temp.jpg")
def deleteRow(tempFile,image_name,path):
    
    name = (os.path.basename(str(image_name)))
    file_name = path + name + '.lines.txt'
    def draw_rect(event, x, y, flags, param):
	# grab references to the global variables
	global ix,iy, cropping

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
    	if event == cv2.EVENT_LBUTTONDOWN:
		    #refPt = [(x, y)]
            ix,iy=x,y
            cv2.imshow("image", image)

	# check to see if the left mouse button was released
	'''elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
    		# the cropping operation is finished
		refPt.append((x, y))'''


		# draw a rectangle around the region of interest
		#cv2.rectangle(image, refPt[0], refPt[1], (0, 0, 255), -1)

    image  = cv2.imread(tempFile)
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 500,800)
    cv2.setMouseCallback("image", draw_rect)
    data = []
    rowPos=[]
    clone = image.copy()

    data = np.loadtxt(file_name)
    data = data[data[:, 1].argsort()]
     #print data
    while(1):
        cv2.imshow("image",image)
        k = cv2.waitKey(20) & 0xFF
        if k == ord('q'):
           break
        elif k == ord('a'):
            a = findIndex2(ix,iy,file_name)
            rowPos.append(a)
            npx = int(data[a][0])
            npy = int(data[a][1])
            npw = int(data[a][2])
            nph = int(data[a][3])
            cv2.rectangle(image, (npx, npy), (npx + npw, npy + nph), [0, 0, 255], 3)
            print "rowPos:"+str(rowPos)
            #print len(data)
            #for i in range(len(rowPos)):

        elif k== ord('r'):
            image = clone.copy()
    #for i in range(len(rowPos)):
    data =  np.delete(data, rowPos, 0)

    data = data[data[:, 1].argsort()]
    cv2.destroyAllWindows()
    np.savetxt(file_name, data, delimiter=' ')



def edit(tempFile,image_name,path):

    name = (os.path.basename(str(image_name)))
    file_name = path + name + '.lines.txt'
    def draw_rect(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping,ix,iy

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
    	if event == cv2.EVENT_LBUTTONDOWN:
            ix,iy = x,y

            cv2.imshow("image", image)
	# check to see if the left mouse button was released



		# draw a rectangle around the region of interest
		#cv2.rectangle(image, refPt[0], (0, 0, 255), -1)

    image  = cv2.imread(tempFile)
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 500,800)
    cv2.setMouseCallback("image", draw_rect)
    data = []
    clone = image.copy()

    data = np.loadtxt(file_name)
     #print data
    while(1):
        cv2.imshow("image",image)
        k = cv2.waitKey(20) & 0xFF
        if k == ord('q'):
           break
        elif k == ord('a'):
            rowPos =0
            #print refPt
            rowPos = findIndex2(ix,iy,file_name)
            #print "rpw pos= "+str(rowPos)


                #for i in range(len(data)):
            npx = int(data[rowPos][0])
            npy = int(data[rowPos][1])
            npw = int(data[rowPos][2])
            nph = int(data[rowPos][3])
            cv2.rectangle(image,(npx,npy),(npx+npw,npy+nph),[0,0,255],3)
            data = np.delete(data, rowPos, 0)
            x,y,w,h = change(image,npx,npy,npw,nph)
            data = np.insert(data,rowPos, np.array([[x,y,w,h]]), axis=0)



        elif k== ord('r'):
            image = clone.copy()
    data = data[data[:, 1].argsort()]
    cv2.destroyAllWindows()
    np.savetxt(file_name, data, delimiter=' ')

def Shift(tempFile,image_name,location):
    path = location
    print tempFile
    name = (os.path.basename(str(image_name)))
    file_name = path + name + '.lines.txt'

    def draw_rect(event, x, y, flags, param):


        global refPt, cropping, ix, iy

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
        if event == cv2.EVENT_LBUTTONDOWN:
            ix, iy = x, y


        cv2.imshow("image", image)
    image = cv2.imread(tempFile)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 500, 800)
    cv2.setMouseCallback("image", draw_rect)
    data = []
    clone = image.copy()

    data = np.loadtxt(file_name)
    # print data
    while (1):
        cv2.imshow("image", image)
        k = cv2.waitKey(20) & 0xFF
        if k == ord('q'):
            break
        elif k == ord('a'):
            rowPos = 0
            # print refPt
            rowPos = findIndex2(ix, iy, file_name)
            print "rpw pos= " + str(rowPos)

            # for i in range(len(data)):
            npx = int(data[rowPos][0])
            npy = int(data[rowPos][1])
            npw = int(data[rowPos][2])
            nph = int(data[rowPos][3])
            cv2.rectangle(image, (npx, npy), (npx + npw, npy + nph), [0, 0, 255], 3)
            data = np.delete(data, rowPos, 0)
            x, y, w, h = shift(image, npx, npy, npw, nph)
            data = np.insert(data, rowPos, np.array([[x, y, w, h]]), axis=0)



        elif k == ord('r'):
            image = clone.copy()
    data = data[data[:, 1].argsort()]
    cv2.destroyAllWindows()
    np.savetxt(file_name, data, delimiter=' ')