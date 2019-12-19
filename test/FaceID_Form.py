# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FaceID_Form.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 477)
        self.faceWindow = QtWidgets.QLabel(Form)
        self.faceWindow.setGeometry(QtCore.QRect(30, 30, 291, 241))
        self.faceWindow.setObjectName("faceWindow")
        self.chooseFaceBtn = QtWidgets.QPushButton(Form)
        self.chooseFaceBtn.setGeometry(QtCore.QRect(380, 40, 161, 31))
        self.chooseFaceBtn.setObjectName("chooseFaceBtn")
        self.addNewBtn = QtWidgets.QPushButton(Form)
        self.addNewBtn.setGeometry(QtCore.QRect(380, 170, 161, 31))
        self.addNewBtn.setObjectName("addNewBtn")
        self.identifyOldBtn = QtWidgets.QPushButton(Form)
        self.identifyOldBtn.setGeometry(QtCore.QRect(380, 240, 161, 31))
        self.identifyOldBtn.setObjectName("identifyOldBtn")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(380, 130, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.outputWindow = QtWidgets.QTextEdit(Form)
        self.outputWindow.setGeometry(QtCore.QRect(20, 330, 521, 131))
        self.outputWindow.setObjectName("outputWindow")

        self.retranslateUi(Form)
        self.chooseFaceBtn.clicked.connect(Form.chooseFace)
        self.addNewBtn.clicked.connect(Form.chooseFace)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "人脸打卡"))
        self.faceWindow.setText(_translate("Form", "选择图片"))
        self.chooseFaceBtn.setText(_translate("Form", "选脸"))
        self.addNewBtn.setText(_translate("Form", "录入新脸"))
        self.identifyOldBtn.setText(_translate("Form", "识别老脸"))
        self.lineEdit.setText(_translate("Form", "请输入新脸的名字"))
