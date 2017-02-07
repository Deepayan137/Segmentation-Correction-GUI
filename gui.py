import sys
from PyQt4 import QtCore, QtGui
import glob, os
from api import request_info,post_info,delete_info
from contents import find
import subprocess
from convert_format import convert
from skew_correction import deskew,manual_deskew
from test import show_image
from segmentation import click_drag, deleteRow,edit,Shift
from new_window import Ui_MainWindow
state = 0
event=0
angle =0.0
id =0
imageName= []
fileName = ''
s=0
path = sys.argv[1]
path2 = sys.argv[2]
tempFile = path+'temp.jpg'
tempFile2 = path2+'skew_temp.jpg'
class ImageViewer(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super(ImageViewer, self).__init__()
        #ImageViewer.__init__(self, parent)
        self.setupUi(self)
        self.host_mac = 'blah blah'

        self.printer = QtGui.QPrinter()
        self.scaleFactor = 0.0
        self.angle = 0.0
        self.picPaths = []
        self.currentPicture = 0
        self.totalPictures = 0

        self.imageLabel = QtGui.QLabel()
        self.imageLabel.setBackgroundRole(QtGui.QPalette.Base)
        self.imageLabel.setSizePolicy(QtGui.QSizePolicy.Ignored,
               QtGui.QSizePolicy.Ignored)

        self.imageLabel.setScaledContents(True)

        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.setCentralWidget(self.scrollArea)

        self.createActions()
        self.createMenus()

        self.setWindowTitle("Image Viewer")
        self.move(50,50)
        self.resize(500, 600)


    def loadImage(self):
        global fileName,path,tempFile,id
        #fileName = QtGui.QFileDialog.getOpenFileName(self, "Open File","/home/deepayan/CVIT_codes/API/","Images (*.png *.jpg *tif)")
        id=request_info(path)
        convert(path)
        files = os.listdir(path)
        for file in files:
            if file.endswith('.jpg'):

                fileName =path+file

        #print fileName
        if fileName:

            image = QtGui.QImage(fileName)


            self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
            path = (os.path.dirname(str(fileName)))+'/'
            self.picPaths = os.listdir(path)
            name = (os.path.basename(str(fileName)))
            #self.currentPicture, self.totalPictures = find(name, path)

            #self.imageLabel.setPixmap(image)
            #self.imageLabel.setScaledContents(True)

            self.scaleFactor = 1.0

            self.printAct.setEnabled(True)
            self.fitToWindowAct.setEnabled(True)
            self.updateActions()

            if not self.fitToWindowAct.isChecked():
                self.imageLabel.adjustSize()

    def open(self,image):
        global fileName,path
        fileName = path+image
        Qimage = QtGui.QImage(path+image)
        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(Qimage))
        self.draw_boxes()

      # print fileName
    def save(self):
        cwd = os.getcwd()
        name = (os.path.basename(str(fileName)))
        subprocess.call('cd /', shell=True)
        subprocess.call('mv' + ' ' + path2 + name + ' ' + path,
            shell=True)
        subprocess.call('mv' + ' ' + path2 + name + '.lines.txt' + ' ' + path,
            shell=True)
        subprocess.call('cd ' + cwd, shell=True)

        test = path2+'*'
        r = glob.glob(test)
        for i in r:
            os.remove(i)
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText("Saved")
        msg.exec_()

    def deskew(self):
        global fileName, tempFile2,state,path2

        if state==0:

            cwd = os.getcwd()
            name = (os.path.basename(str(fileName)))
            path = path2 + name + '.lines.txt'
            if os.path.exists(path):
                os.remove(path)

            deskew(str(fileName),path2)
            Qimage = QtGui.QImage(tempFile2)
            self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(Qimage))


            #choice=msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            choice = QtGui.QMessageBox.question(self, 'Save or not to save',
                                                "Want to proceed?",
                                                QtGui.QMessageBox.Yes|QtGui.QMessageBox.Cancel)



            cwd = os.getcwd()
            name = (os.path.basename(str(fileName)))
            if choice == QtGui.QMessageBox.Yes:
               self.save()
            elif choice == QtGui.QMessageBox.Cancel:

                Qimage = QtGui.QImage(fileName)

                self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(Qimage))

                self.imageLabel.setScaledContents(True)



    def restoration(self):
        global tempFile
        # areaClose(str(tempFile))

        pixmap = QtGui.QPixmap(fileName)

        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setScaledContents(True)
    def draw_boxes(self):
        global fileName,tempFile,s

        '''if os.path.exists(str(fileName) + '.lines.txt')== False:
            #if  os.path.exists(str(fileName) + '.blocks.txt')== False:
             box(str(fileName))'''

        show_image(str(fileName),s)

        pixmap = QtGui.QPixmap(tempFile)
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setScaledContents(True)

    def mouseRemove(self):
        global tempFile, fileName, state

        # deleteRow(str(tempFile2),str(fileName+'.lines.txt'))
        if state == 0:
            deleteRow(str(tempFile), str(fileName))
        elif state == 1:
            deleteRow(str(tempFile), str(fileName))

    def nextPicture(self):

       """
       Loads the next picture in the directory
       """



    def previousPicture(self):

       """
       Displays the previous picture in the directory

       """
       '''for root, dirs, files in os.walk(path):
           for file in files:
               if file.endswith(".txt"):
                   self.delete(file)'''
       if self.currentPicture == 0:
           self.currentPicture = self.totalPictures
       else:
           self.currentPicture -= 1
       while(1):
        if self.picPaths[self.currentPicture].endswith('.jpg'):

            self.open(self.picPaths[self.currentPicture])
            #box(self.picPaths[self.currentPicture])
            break

    def onNext(self, event):
       """
       Calls the nextPicture method
       """

       global fileName,id,path
       text_file = fileName+'.lines.txt'
       status = post_info(id,fileName,text_file,path)
       print status
       if status == 1:
           msg = QtGui.QMessageBox()
           msg.setIcon(QtGui.QMessageBox.Information)
           msg.setText("Post was Succesfull")

           msg.exec_()
           #self.loadImage()
       elif status == 2:
           msg = QtGui.QMessageBox()
           msg.setIcon(QtGui.QMessageBox.Information)
           msg.setText("ERROR")
           msg.exec_()
       elif status == 3:
           msg = QtGui.QMessageBox()
           msg.setIcon(QtGui.QMessageBox.Information)
           msg.setText("BAD METHOD\n Try Again")
           msg.exec_()

       #subprocess.call('cd /', shell=True)
       #subprocess.call('mv' + ' ' + fileName + ' ' + '/home/deepayan/codes_seg/data/Correct/', shell=True)
       #subprocess.call('cd ' + cwd, shell=True)
       self.nextPicture()

    def onPrevious(self, event):
       """
       Calls the nextPicture method
       """
       self.previousPicture()

    def delete(self):
        global fileName,id,path
        status = delete_info(id, fileName, path)
        print status
        if status == 1:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("File is removed")

            msg.exec_()
            # self.loadImage()
        elif status == 2:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("ERROR")
            msg.exec_()
        elif status == 3:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("BAD METHOD\n Try Again")
            msg.exec_()



    def remove(self):
        global  fileName
        #print fileName
        cwd = os.getcwd()
        subprocess.call('cd /', shell=True)
        subprocess.call('mv'+' '+fileName+' '+'/home/deepayan/codes_seg/data/wrong/', shell=True)
        subprocess.call('cd ' + cwd, shell=True)
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText("file removed")
        msg.exec_()


    def skewPositive(self):
        self.scaleSkew(0.1)

    def skewNegative(self):
        self.scaleSkew(-0.1)
    def zoomIn(self):
       self.scaleImage(1.25)

    def zoomOut(self):
       self.scaleImage(0.8)

    def normalSize(self):
       self.imageLabel.adjustSize()
       # self.scaleFactor = 1.0

    def mouseDraw(self, factor):
        global tempFile, fileName, state
        if state == 0:
            click_drag(str(tempFile), str(fileName))
        elif state == 1:
            click_drag(str(tempFile), str(fileName))

    def mouseEdit(self):
        global fileName,tempFile,state,path
        if state == 0:
            edit(str(tempFile), str(fileName),path)
        elif state == 1:
            edit(str(tempFile), str(fileName),path)
    def mouseShift(self):

        global fileName,tempFile, state,path
        print str(fileName)
        if state == 0:
            Shift(str(tempFile), str(fileName),path)
        elif state == 1:
            Shift(str(tempFile), str(fileName))

    def fitToWindow(self):
       fitToWindow = self.fitToWindowAct.isChecked()
       self.scrollArea.setWidgetResizable(fitToWindow)
       if not fitToWindow:
           self.normalSize()

       self.updateActions()
    def print_(self):
        dialog = QtGui.QPrintDialog(self.printer, self)
        if dialog.exec_():
            painter = QtGui.QPainter(self.printer)
            rect = painter.viewport()
            size = self.imageLabel.pixmap().size()
            size.scale(rect.size(), QtCore.Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.imageLabel.pixmap().rect())
            painter.drawPixmap(0, 0, self.imageLabel.pixmap())

    def about(self):
       QtGui.QMessageBox.about(self, "About Image Viewer",
                               "<p>The <b>Image Viewer</b> example shows how to combine "
                               "QLabel and QScrollArea to display an image. QLabel is "
                               "typically used for displaying text, but it can also display "
                               "an image. QScrollArea provides a scrolling view around "
                               "another widget. If the child widget exceeds the size of the "
                               "frame, QScrollArea automatically provides scroll bars.</p>"
                               "<p>The example demonstrates how QLabel's ability to scale "
                               "its contents (QLabel.scaledContents), and QScrollArea's "
                               "ability to automatically resize its contents "
                               "(QScrollArea.widgetResizable), can be used to implement "
                               "zooming and scaling features.</p>"
                               "<p>In addition the example shows how to use QPainter to "
                               "print an image.</p>")

    def wind(self):
        global fileName
        print "triggered"
        #sh("/home/deepayan/CVIT_codes/GUI/second_win_2.py")
        output=subprocess.check_output('python' + ' ' + '/home/deepayan/CVIT_codes/GUI/new_window.py', shell=True)
        checked=int(output.split('.')[0])
        s = checked
        show_image(fileName,s)


        #print './j-layout ' + fileName + ' ' + '-psm' + ' ' + checked
        #self.mySubwindow = new_window.MainWindow()
        #self.mySubwindow.btnstate()
        #self.mySubwindow.show()





    def createActions(self):
       self.openAct = QtGui.QAction("&Open...", self, shortcut="Ctrl+O",
                                    triggered=self.loadImage)

       self.printAct = QtGui.QAction("&Print...", self, shortcut="Ctrl+P",
                                     enabled=False, triggered=self.print_)

       self.exitAct = QtGui.QAction("&Exit", self, shortcut="Ctrl+Q",
                                    triggered=self.close)

       self.zoomInAct = QtGui.QAction("Zoom &In (25%)", self,
                                      shortcut="Ctrl++", enabled=False, triggered=self.zoomIn)
       self.skewPositiveAct = QtGui.QAction("Skew &Positive (0.1)", self,
                                      shortcut="Ctrl+P", enabled=True, triggered=self.skewPositive)
       self.saveAct = QtGui.QAction("Save", self,
                                            shortcut="Ctrl+S", enabled=True, triggered=self.save)

       self.zoomOutAct = QtGui.QAction("Zoom &Out (25%)", self,
                                       shortcut="Ctrl+-", enabled=True, triggered=self.zoomOut)
       self.skewNegativeAct= QtGui.QAction("skew &Negative (-0.1)", self,
                                      shortcut="Ctrl+N", enabled=True, triggered=self.skewNegative)

       self.normalSizeAct = QtGui.QAction("&Normal Size", self,
                                          shortcut="Ctrl+F", enabled=False, triggered=self.normalSize)

       self.fitToWindowAct = QtGui.QAction("&Fit to Window", self,
                                           enabled=False, checkable=True, shortcut="Ctrl+F",
                                           triggered=self.fitToWindow)

       self.aboutAct = QtGui.QAction("&About", self, triggered=self.about)

       self.aboutQtAct = QtGui.QAction("About &Qt", self,
                                       triggered=QtGui.qApp.aboutQt)
       # self.openAct = QtGui.QAction("&Open",self,triggered = self.open)
       self.onNextAct  =  QtGui.QAction("Post", self,
                                       triggered=self.onNext)
       self.onPreviousAct = QtGui.QAction("Previous", self,
                                       triggered=self.onPrevious)
       self.moveAct = QtGui.QAction("Move", self,
                                          triggered=self.remove)
       self.mouseDrawAct = QtGui.QAction("&Draw", self,
                                            triggered=self.mouseDraw)
       self.segmentAct = QtGui.QAction("Segment", self,
                                       triggered=self.draw_boxes)

       #self.mouseRemoveAct = QtGui.QAction("&Restore", self, triggered=self.restoration)
       #self.mouseRemoveAct = QtGui.QAction("&Remove", self, triggered=self.mouseRemove)
       self.mouseEditAct = QtGui.QAction("&Edit", self, triggered=self.mouseEdit)
       self.mouseShiftAct = QtGui.QAction("&Shift", self, triggered=self.mouseShift)
       self.trashAct = QtGui.QAction("&Trash", self, triggered=self.delete)

       self.deskewAct = QtGui.QAction("&Deskew", self,triggered=self.deskew)
       self.windAct = QtGui.QAction("&Wind", self,triggered=self.wind)

    def createMenus(self):
       self.fileMenu = QtGui.QMenu("&File", self)
       self.toolbar = QtGui.QToolBar(self)
       self.toolBar = self.addToolBar(self.toolbar)
       self.fileMenu.addAction(self.openAct)
       self.fileMenu.addAction(self.printAct)
       self.fileMenu.addSeparator()
       self.fileMenu.addAction(self.exitAct)

       self.viewMenu = QtGui.QMenu("&View", self)
       self.viewMenu.addAction(self.zoomInAct)
       self.viewMenu.addAction(self.zoomOutAct)
       self.viewMenu.addAction(self.normalSizeAct)
       self.viewMenu.addSeparator()
       self.viewMenu.addAction(self.fitToWindowAct)

       self.helpMenu = QtGui.QMenu("&Help", self)
       self.helpMenu.addAction(self.aboutAct)
       self.helpMenu.addAction(self.aboutQtAct)
       self.testMenu = QtGui.QMenu("&Test", self)
       self.testMenu.addAction(self.windAct)
       self.skewMenu = QtGui.QMenu("&Deskew",self)
       self.skewMenu.addAction(self.skewPositiveAct)
       self.skewMenu.addAction(self.skewNegativeAct)
       self.skewMenu.addAction(self.saveAct)
       # self.linesMenu = QtGui.QMenu("&Lines",self)
       # self.linesMenu.addAction(self.segmentAct)

       self.menuBar().addMenu(self.fileMenu)
       self.menuBar().addMenu(self.viewMenu)
       self.menuBar().addMenu(self.helpMenu)
       self.menuBar().addMenu(self.skewMenu)
       self.menuBar().addMenu(self.testMenu)
       #self.toolbar.addAction(self.restorationAct)
       self.toolbar.addAction(self.onNextAct)
       #self.toolbar.addAction(self.onPreviousAct)
       self.toolbar.addAction(self.moveAct)
       self.toolbar.addAction(self.mouseDrawAct)
       self.toolbar.addAction(self.segmentAct)
       #self.toolbar.addAction(self.mouseRemoveAct)
       self.toolbar.addAction(self.mouseEditAct)
       self.toolbar.addAction(self.mouseShiftAct)
       self.toolbar.addAction(self.trashAct)
       self.toolbar.addAction(self.deskewAct)

    def updateActions(self):
       self.zoomInAct.setEnabled(not self.fitToWindowAct.isChecked())
       self.zoomOutAct.setEnabled(not self.fitToWindowAct.isChecked())
       self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())
    def scaleSkew(self,factor):
        global fileName,tempFile2,path2
        name = (os.path.basename(str(fileName)))
        path = path2+name+'.lines.txt'
        cwd = os.getcwd()
        if os.path.exists(path):
            os.remove(path)

        self.angle += factor
        manual_deskew(str(fileName),self.angle,path2)
        Qimage = QtGui.QImage(str(tempFile2))

        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(Qimage))

        self.imageLabel.setScaledContents(True)

    def scaleImage(self, factor):
       self.scaleFactor *= factor
       self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

       self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
       self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

       self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
       self.zoomOutAct.setEnabled(self.scaleFactor > 0.333)

    def adjustScrollBar(self, scrollBar, factor):
       scrollBar.setValue(int(factor * scrollBar.value()))
       # + ((factor - 1) * scrollBar.pageStep()/2)))


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    imageViewer = ImageViewer()
    imageViewer.show()
    sys.exit(app.exec_())
