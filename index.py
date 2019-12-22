import sys, os

import cv2
from PyQt5.QtGui import QImage, QPixmap

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import asyncio
from PyQt5 import QtWidgets,QtGui,QtMultimedia,QtCore
from PyQt5.QtWidgets import QFileDialog
from apis.register import addUser
from apis.identify import identify
from apis.delUser import queryMember,delUser
from apis.queryMembers import getAllUsers
from apis.audio import speak
from IndexUI import Ui_TabWidget

class Main_Form(QtWidgets.QTabWidget,Ui_TabWidget):
    def __init__(self):
        super(Main_Form,self).__init__()
        self.setupUi(self)
        self.player = QtMultimedia.QMediaPlayer()

    def videoCapture(self):
        # 0是代表摄像头编号，只有一个的话默认为0
        self.capture = cv2.VideoCapture(0)
        # self.capture.open()
        while (True):
            # self.capture = cv2.VideoCapture(0)
            ref, frame = self.capture.read()
            height, width, bytesPerComponent = frame.shape
            bytesPerLine = bytesPerComponent * width
            # 变换彩色空间顺序
            cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
            # 转为QImage对象
            self.image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.faceIdentification_label.setPixmap(QPixmap.fromImage(self.image))
            # print(type(self.image))
            # cv2.imshow("1", frame)
            # 等待30ms显示图像，若过程中按“Esc”退出
            c = cv2.waitKey(30) & 0xff
            if c == 27:
                # print(type(self.image))
                self.capture.release()
                break
        cv2.waitKey(0)
    def iden(self):
        if self.image:
            self.player = QtMultimedia.QMediaPlayer()
            idResult = identify(self.image)
            self.clockInRecordsList.addItem(idResult)
            # Python 3.7+
            asyncio.run(speak(self.player,idResult))
        # self.capture.release()
    def chooseFace(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.faceIdentification_label.width(), self.faceIdentification_label.height())
        self.faceIdentification_label.setPixmap(jpg)
        # self.clockInRecordsList.addItem(addUser(imgName,'hahahaha'))
        # print(addUser(imgName,'hahahaha'))
        self.imgName =imgName

    def identifyClockIn(self):
        if self.imgName:
            idResult = identify(self.imgName)
            self.clockInRecordsList.addItem(idResult)
            # Python 3.7+
            asyncio.run(speak(self.player,idResult))


    def chooseFaceToAdd(self):
        imgAddName, imgAddType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgAddName).scaled(self.faceAddition_label.width(),
                                            self.faceAddition_label.height())
        self.faceAddition_label.setPixmap(jpg)
        self.imgAddName = imgAddName

    def addFaceName_changed(self):
        self.textAddName = self.addFaceName_lineEdit.text().strip()

    def addFaceID_changed(self):
        self.textAddID = self.addFaceID_lineEdit.text().strip()

    def signUpFace(self):
        if self.imgAddName and self.textAddName and self.textAddID:
            res = addUser(self.imgAddName,self.textAddID,self.textAddName)
            self.blackboardAdd_textEidt.setText(res)

    def delFaceID_changed(self):
        self.textDelID = self.delFaceID_lineEdit.text().strip()

    def delMemberQuery(self):
        if self.textDelID:
            res = queryMember(self.textDelID)
            self.faceDeletion_label.setText(res)

    def delMember(self):
        if self.textDelID:
            res = delUser(self.textDelID)
            self.blackboardDel_textEidt.setText(res)

    def queryMembers(self):
        res = getAllUsers()
        for i in res:
            self.membersQuery_listWidget.addItem(i)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_form = Main_Form()
    main_form.show()
    sys.exit(app.exec_())