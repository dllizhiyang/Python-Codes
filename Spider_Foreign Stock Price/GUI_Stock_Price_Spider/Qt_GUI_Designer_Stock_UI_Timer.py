# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt_GUI_Designer_Stock_UI_Timer.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Qt_Designer_StockPrice
import threading
global Timing
global eachTime
eachTime = 5



class Ui_MainWindow(object):
##########################在中间插入另外文件中的函数。更改click事件#######################################
    def showNintendoPrice(self):
        self.label_4.setText('%s'%(Qt_Designer_StockPrice.getNintendoStockPrice()))
    def showLGPrice(self):
        self.label_5.setText('%s'%(Qt_Designer_StockPrice.getLGStockPrice1()))
    def showTencentPrice(self):
        self.label_6.setText('%s'%(Qt_Designer_StockPrice.getTencentStockPrice()))

##################################加入定时刷新函数########################################################
    def refreshNintendoPrice(self):
        Timing = threading.Timer(eachTime,self.showNintendoPrice)
        Timing.start()
    def refreshLGPrice(self):
        Timing = threading.Timer(eachTime,self.showLGPrice)
        Timing.start()
    def refreshTencentPrice(self):
        Timing = threading.Timer(eachTime,self.showTencentPrice)
        Timing.start()


###########################################################################################################
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 400, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 80, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 160, 131, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 160, 121, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(530, 160, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 400, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.refreshNintendoPrice)
        self.pushButton.clicked.connect(self.showLGPrice)
        self.pushButton.clicked.connect(self.showTencentPrice)
        self.pushButton_2.clicked.connect(self.label_6.clear)
        self.pushButton_2.clicked.connect(self.label_5.clear)
        self.pushButton_2.clicked.connect(self.label_4.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "5秒刷新"))
        self.label.setText(_translate("MainWindow", "Nintendo"))
        self.label_2.setText(_translate("MainWindow", "LG"))
        self.label_3.setText(_translate("MainWindow", "Tencent"))
        self.label_4.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "停"))

##########################################启动主函数############################################
import sys
import Qt_GUI_Designer_Stock_UI
from PyQt5.QtWidgets import QApplication, QMainWindow
import Qt_GUI_Designer_Stock_UI_Timer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui1 = Qt_GUI_Designer_Stock_UI_Timer.Ui_MainWindow()
    ui1.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    Timing = threading.Timer(eachTime,self.showNintendoPrice())
    Timing.start()
    Timing = threading.Timer(eachTime,self.showLGPrice())
    Timing.start()
    Timing = threading.Timer(eachTime,self.showTencentPrice())
    Timing.start()


################################################################################################

