# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
filename = '~/temp1/'
import subprocess
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        parent = None
        super(Ui_MainWindow, self).__init__()
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 100, 721, 421))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radioButton = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton.setChecked(False)
        self.radioButton.toggled.connect(lambda: self.btnstate(self.radioButton))
        self.horizontalLayout_4.addWidget(self.radioButton)
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.radioButton_2 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_2.toggled.connect(lambda: self.btnstate(self.radioButton_2))
        self.horizontalLayout_5.addWidget(self.radioButton_2)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.radioButton_3 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_3.toggled.connect(lambda: self.btnstate(self.radioButton_3))
        self.horizontalLayout_6.addWidget(self.radioButton_3)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.radioButton_4 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_4.toggled.connect(lambda: self.btnstate(self.radioButton_4))
        self.horizontalLayout_7.addWidget(self.radioButton_4)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_7.addWidget(self.label_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.radioButton_5 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.radioButton_5.toggled.connect(lambda: self.btnstate(self.radioButton_5))
        self.horizontalLayout_8.addWidget(self.radioButton_5)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_8.addWidget(self.label_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.radioButton_6 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.radioButton_6.toggled.connect(lambda: self.btnstate(self.radioButton_6))
        self.horizontalLayout_9.addWidget(self.radioButton_6)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_9.addWidget(self.label_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.radioButton_7 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.radioButton_7.toggled.connect(lambda: self.btnstate(self.radioButton_7))
        self.horizontalLayout_10.addWidget(self.radioButton_7)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_10.addWidget(self.label_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.radioButton_8 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.radioButton_8.toggled.connect(lambda: self.btnstate(self.radioButton_8))
        self.horizontalLayout_11.addWidget(self.radioButton_8)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_11.addWidget(self.label_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.radioButton_9 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_9.setObjectName(_fromUtf8("radioButton_9"))
        self.radioButton_9.toggled.connect(lambda: self.btnstate(self.radioButton_9))
        self.horizontalLayout_12.addWidget(self.radioButton_9)
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_12.addWidget(self.label_9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.radioButton_10 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_10.setEnabled(True)
        self.radioButton_10.setObjectName(_fromUtf8("radioButton_10"))
        self.radioButton_10.toggled.connect(lambda: self.btnstate(self.radioButton_10))
        self.horizontalLayout_15.addWidget(self.radioButton_10)
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_15.addWidget(self.label_12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.radioButton_11 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_11.setObjectName(_fromUtf8("radioButton_11"))
        self.radioButton_11.toggled.connect(lambda: self.btnstate(self.radioButton_11))
        self.horizontalLayout_14.addWidget(self.radioButton_11)
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_14.addWidget(self.label_11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        #self.groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        #self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton("Quit")
        self.pushButton.setGeometry(QtCore.QRect(100, 0, 89, 27))
        self.pushButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        #self.pushButton_2.setGeometry(QtCore.QRect(100, 0, 89, 27))
        #self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_3.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.radioButton.setText(_translate("MainWindow", "1.", None))
        self.label.setText(_translate("MainWindow", "Orientation and script detection (OSD) only", None))
        self.radioButton_2.setText(_translate("MainWindow", "2.", None))
        self.label_2.setText(_translate("MainWindow", "Automatic page segmentation with OSD.", None))
        self.radioButton_3.setText(_translate("MainWindow", "3.", None))
        self.label_3.setText(_translate("MainWindow", "Automatic page segmentation, but no OSD, or OCR.", None))
        self.radioButton_4.setText(_translate("MainWindow", "4.", None))
        self.label_4.setText(_translate("MainWindow", "Fully automatic page segmentation, but no OSD. (Default)", None))
        self.radioButton_5.setText(_translate("MainWindow", "5.", None))
        self.label_5.setText(_translate("MainWindow", "Assume a single column of text of variable sizes.", None))
        self.radioButton_6.setText(_translate("MainWindow", "6.", None))
        self.label_6.setText(_translate("MainWindow", "Assume a single uniform block of vertically aligned text.", None))
        self.radioButton_7.setText(_translate("MainWindow", "7.", None))
        self.label_7.setText(_translate("MainWindow", "Assume a single uniform block of text.", None))
        self.radioButton_8.setText(_translate("MainWindow", "8.", None))
        self.label_8.setText(_translate("MainWindow", "Treat the image as a single text line.", None))
        self.radioButton_9.setText(_translate("MainWindow", "9.", None))
        self.label_9.setText(_translate("MainWindow", "Treat the image as a single word.", None))
        self.radioButton_10.setText(_translate("MainWindow", "10.", None))
        self.label_12.setText(_translate("MainWindow", "Treat the image as a single word in a circle.", None))
        self.radioButton_11.setText(_translate("MainWindow", "11.", None))
        self.label_11.setText(_translate("MainWindow", "Treat the image as a single character.", None))
        #self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))

        #self.pushButton_2.setText(_translate("MainWindow", "Cancel", None))

    def btnstate(self, b):
        global fileName
        if b.text() == "1.":
            if b.isChecked() == True:
                print b.text()



        if b.text() == "2.":
            if b.isChecked() == True:
                print b.text()
        if b.text() == "3.":
            if b.isChecked() == True:
                print b.text()
        if b.text() == "4.":
            if b.isChecked() == True:
                print b.text()
        if b.text() == "5.":
            if b.isChecked() == True:
                print b.text()
        if b.text() == "6.":
            if b.isChecked() == True:
                print b.text()
        if b.text() == "7.":
            if b.isChecked() == True:
                print b.text()
        if b.text() == "8.":
            if b.isChecked() == True:
                print b.text()
        if b.text() == "9.":
            if b.isChecked() == True:
                print b.text()
        if b.text() == "10.":
            if b.isChecked() == True:
                print b.text()
        if b.text() == "11.":
            if b.isChecked() == True:
                print b.text()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

