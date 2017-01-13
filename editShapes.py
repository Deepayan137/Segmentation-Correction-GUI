import cv2
import numpy as np


drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
def draw():
# mouse callback function
    def draw_circle(event,x,y,flags,param):
        global ix,iy,jx,jy,drawing,mode

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix,iy = x,y

        '''elif event == cv2.EVENT_MOUSEMOVE:
            if drawing == True: data = np.array([[x,y,w,h]])
    np.savetxt('temp.txt',data,delimiter=' ')
    while (1):
        #clone = image.copy()

        cv2.imshow('image', image)
        k = cv2.waitKey(0) & 0xFF
        if k == (27):
            break
        elif k == ord('d'):
            clone = image.copy()
            arr = np.loadtxt('temp.txt')
            arr[2] = arr[2] +15
            np.savetxt('temp.txt', arr, delimiter=' ')
            arr = (np.loadtxt('temp.txt'))
            x1 = int(arr[0])
            y1 = int(arr[1])
            x2 = int(arr[0] + arr[2])
            y2 = int(arr[1] + arr[3])

            cv2.rectangle(clone, (x1,y1), (x2,y2), [0,255,0], 3)
            #cv2.imwrite('clone.png',clone)
            cv2.imshow('image', clone)
            cv2.waitKey(0)
        elif k == ord('s'):
            clone = image.copy()
            arr = np.loadtxt('temp.txt')
            #arr[1] = arr[1] -15
            arr[3] = arr[3]+15
            np.savetxt('temp.txt', arr, delimiter=' ')
            arr = (np.loadtxt('temp.txt'))
            x1 = int(arr[0])
            y1 = int(arr[1])
            x2 = int(arr[0] + arr[2])
            y2 = int(arr[1] + arr[3])


            cv2.rectangle(clone, (x1, y1), (x2,y2), [0, 255, 0], 3)
            cv2.imshow('image', clone)
            cv2.waitKey(0)

        elif k == ord('w'):
            clone = image.copy()
            arr = np.loadtxt('temp.txt')
            arr[1] = arr[1] -15
            arr[3] = arr[3]+15
            np.savetxt('temp.txt', arr, delimiter=' ')
            arr = (np.loadtxt('temp.txt'))
            x1 = int(arr[0])
            y1 = int(arr[1])
            x2 = int(arr[0] + arr[2])
            y2 = int(arr[1] + arr[3])

            cv2.rectangle(clone, (x1, y1), (x2, y2), [0, 255, 0], 3)
            # cv2.imwrite('clone.png',clone)
            cv2.imshow('image', clone)
            cv2.waitKey(0)
        elif k == ord('a'):
            clone = image.copy()
            arr = np.loadtxt('temp.txt')

            arr[0] = arr[0] - 15
            arr[2] = arr[2] + 15
            np.savetxt('temp.txt', arr, delimiter=' ')
            arr = (np.loadtxt('temp.txt'))
            x1 = int(arr[0])
            y1 = int(arr[1])
            x2 = int(arr[0] + arr[2])
            y2 = int(arr[1] + arr[3])

            cv2.rectangle(clone, (x1, y1), (x2, y2), [0, 255, 0], 3)
            # cv2.imwrite('clone.png',clone)
            cv2.imshow('image', clone)
            cv2.waitKey(0)


    cv2.destroyAllWindows()
    return x1,y1,(x2-x1),(y2-y1)
    #edit('temp_image.jpg',fileName)
                if mode == True:
                    cv2.line(img,(ix,iy),(x,y),(0,255,0),2)
                else:
                    cv2.circle(img,(x,y),5,(0,0,255),2)'''

        if event == cv2.EVENT_LBUTTONUP:
            drawing = False
            if mode == True:
                jx = x
                jy = y

                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)

            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), 2)


    img = (np.zeros((512,512,3), np.uint8))
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)
    file = 'boxes.txt'
    data =[]
    data = np.loadtxt(file)
   # print len(data)
    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        if k == ord('a'):
            #print len([ix, iy, (jx-ix), (jy-iy)])
            data = np.append(data, np.array([[ix, iy, (jx-ix), (jy-iy)]]), axis=0)
        elif k == 27:
            break

    cv2.destroyAllWindows()
    np.savetxt(file,data,delimiter=' ')
    cv2.imwrite('shapes.jpg',img)

#draw()
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
def shift(image,x,y,w,h):
    data = np.array([[x, y, w, h]])
    np.savetxt('temp.txt', data, delimiter=' ')
    while (1):
        # clone = image.copy()

        cv2.imshow('image', image)
        k = cv2.waitKey(0) & 0xFF
        if k == (27):
            break
        elif k == ord('d'):
            clone = image.copy()
            arr = np.loadtxt('temp.txt')
            arr[0] = arr[0] + 15
            np.savetxt('temp.txt', arr, delimiter=' ')
            arr = (np.loadtxt('temp.txt'))
            x1 = int(arr[0])
            y1 = int(arr[1])
            x2 = int(arr[0] + arr[2])
            y2 = int(arr[1] + arr[3])

            cv2.rectangle(clone, (x1, y1), (x2, y2), [0, 255, 0], 3)
            # cv2.imwrite('clone.png',clone)
            cv2.imshow('image', clone)
            cv2.waitKey(0)
        elif k == ord('s'):
            clone = image.copy()
            arr = np.loadtxt('temp.txt')
            # arr[1] = arr[1] -15
            arr[1] = arr[1] + 15
            np.savetxt('temp.txt', arr, delimiter=' ')
            arr = (np.loadtxt('temp.txt'))
            x1 = int(arr[0])
            y1 = int(arr[1])
            x2 = int(arr[0] + arr[2])
            y2 = int(arr[1] + arr[3])

            cv2.rectangle(clone, (x1, y1), (x2, y2), [0, 255, 0], 3)
            cv2.imshow('image', clone)
            cv2.waitKey(0)

        elif k == ord('w'):
            clone = image.copy()
            arr = np.loadtxt('temp.txt')
            arr[1] = arr[1] - 15
            #arr[3] = arr[3] + 15
            np.savetxt('temp.txt', arr, delimiter=' ')
            arr = (np.loadtxt('temp.txt'))
            x1 = int(arr[0])
            y1 = int(arr[1])
            x2 = int(arr[0] + arr[2])
            y2 = int(arr[1] + arr[3])

            cv2.rectangle(clone, (x1, y1), (x2, y2), [0, 255, 0], 3)
            # cv2.imwrite('clone.png',clone)
            cv2.imshow('image', clone)
            cv2.waitKey(0)
        elif k == ord('a'):
            clone = image.copy()
            arr = np.loadtxt('temp.txt')

            arr[0] = arr[0] - 15
            #arr[2] = arr[2] + 15
            np.savetxt('temp.txt', arr, delimiter=' ')
            arr = (np.loadtxt('temp.txt'))
            x1 = int(arr[0])
            y1 = int(arr[1])
            x2 = int(arr[0] + arr[2])
            y2 = int(arr[1] + arr[3])

            cv2.rectangle(clone, (x1, y1), (x2, y2), [0, 255, 0], 3)
            # cv2.imwrite('clone.png',clone)
            cv2.imshow('image', clone)
            cv2.waitKey(0)

    cv2.destroyAllWindows()
    return x1, y1, (x2 - x1), (y2 - y1)
    # edit('temp_image.jpg',fileName)

def change(image_path,x,y,w,h):

    #data = np.array([[x,y,w,h]])
    #np.savetxt('temp.txt',data,delimiter=' ')
    x1 = x
    y1 = y
    x2 = x+w
    y2 = y+h

    def draw_rect(event, x, y, flags, param):

        global refPt, cropping, ix, iy

        # if the left mouse button was clicked, record the starting
        # (x, y) coordinates and indicate that cropping is being
        # performed
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(image, (x, y), 2, (255, 0, 0), -1)
            ix, iy = x, y

            cv2.imshow("image", image)




    image= cv2.imread(image_path)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 500, 800)
    cv2.setMouseCallback("image", draw_rect)

    while (1):
        cv2.imshow('image', image)
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            break
        elif k == ord('a'):
            clone = image.copy()

            if ix > x2 or iy > y2:
                x2= np.max((x2,ix))
                y2=np.max((y2,iy))
                cv2.rectangle(clone, (x1,y1),(x2,y2),[0, 255, 0], 3)
                #print x1,y1,np.max(x2,ix),np.max(y2,iy)
                # cv2.imwrite('clone.png',clone)
                cv2.imshow('image', clone)
                cv2.waitKey(0)
            elif iy < y1 or ix < x1:
                x1 = np.min((x1,ix))
                y1 = np.min((y1,iy))

                cv2.rectangle(clone,(x1,y1),(x2,y2), [0, 255, 0], 3)
                # cv2.imwrite('clone.png',clone)
                cv2.imshow('image', clone)
                cv2.waitKey(0)


    cv2.destroyAllWindows()

    return x1, y1, (x2 - x1), (y2 - y1)



def edit(imageName,fileName):

    def draw_rect(event, x, y, flags, param):
        # grab references to the global variables
        global ix, iy, jx, jy
        global refPt, cropping

        if event == cv2.EVENT_LBUTTONDOWN:
            ix,iy = x,y
            refPt = [ix,iy]
        cv2.circle(image, (ix,iy),20, (0, 0, 255), -2)

        cv2.imshow('image',image)


    image = cv2.imread(imageName)

    # clone = image.copy()
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 500, 800)
    cv2.setMouseCallback('image',draw_rect)

    clone = image.copy()
    data = np.loadtxt(fileName)
        # print data
    while (1):

        cv2.imshow('image', image)
        #cv2.imshow('image',image)
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            break
        elif k == ord('a'):
            rowPos = findIndex2(ix,iy, fileName)
            print rowPos

            for i in range(len(rowPos)):
                data[rowPos[i]][0]= data[rowPos[i]][0]+50.0
            #print len(data)
        elif k == ord('r'):
            image = clone.copy()
    cv2.destroyAllWindows()
    np.savetxt(fileName,data,delimiter=' ')

#edit('temp_image.jpg','/home/deepayan/codes_seg/set2/00000010.jpg.lines.txt')
