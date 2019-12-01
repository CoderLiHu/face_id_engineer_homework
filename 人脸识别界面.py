 # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '人脸识别界面.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(672, 457)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(30, 40, 451, 291))
        self.graphicsView.setObjectName("graphicsView")
        self.chooseFaceBtn = QtWidgets.QPushButton(Form)
        self.chooseFaceBtn.setGeometry(QtCore.QRect(510, 40, 131, 41))
        self.chooseFaceBtn.setObjectName("chooseFaceBtn")
        self.addNewBtn = QtWidgets.QPushButton(Form)
        self.addNewBtn.setGeometry(QtCore.QRect(510, 220, 131, 41))
        self.addNewBtn.setObjectName("addNewBtn")
        self.recognizeBtn = QtWidgets.QPushButton(Form)
        self.recognizeBtn.setGeometry(QtCore.QRect(510, 290, 131, 41))
        self.recognizeBtn.setObjectName("recognizeBtn")
        self.nameInput = QtWidgets.QLineEdit(Form)
        self.nameInput.setGeometry(QtCore.QRect(510, 159, 131, 41))
        self.nameInput.setObjectName("nameInput")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 370, 611, 61))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "人脸打卡"))
        self.chooseFaceBtn.setText(_translate("Form", "选     脸"))
        self.chooseFaceBtn.clicked.connect(self.openimage)
        self.addNewBtn.setText(_translate("Form", "录 入 新 脸"))
        self.recognizeBtn.setText(_translate("Form", "识 别 打 卡"))
        self.nameInput.setText(_translate("Form", "请输入姓名"))
        self.textBrowser.setText(_translate("Form", "哈哈哈"))

    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.graphicsView.width(), self.graphicsView.height())
        self.graphicsView.setPixmap(jpg)

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())