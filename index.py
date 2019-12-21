import sys
from PyQt5 import QtWidgets,QtGui,QtMultimedia,QtCore
from PyQt5.QtWidgets import QFileDialog

from apis.test import test_face
from apis.register import addUser
from apis.identify import identify
from apis.delUser import queryMember,delUser
from IndexUI import Ui_TabWidget

class Main_Form(QtWidgets.QTabWidget,Ui_TabWidget):
    def __init__(self):
        super(Main_Form,self).__init__()
        self.setupUi(self)

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
            url = QtCore.QUrl.fromLocalFile(
                r"D:\myPython\face_id_engineer_homework\apis\auido.mp3")
            content = QtMultimedia.QMediaContent(url)
            player = QtMultimedia.QMediaPlayer()
            player.setMedia(content)
            player.setVolume(50.0)
            player.play()


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
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_form = Main_Form()
    main_form.show()
    sys.exit(app.exec_())