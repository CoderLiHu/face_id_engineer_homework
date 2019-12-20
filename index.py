import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QFileDialog

from apis.test import test_face
from apis.register import addUser
from apis.identify import identify
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
            self.clockInRecordsList.addItem(identify(self.imgName))


    def chooseFaceToAdd(self):
        imgAddName, imgAddType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgAddName).scaled(self.faceAddition_label.width(),
                                            self.faceAddition_label.height())
        self.faceAddition_label.setPixmap(jpg)
        self.imgAddName = imgAddName

    def iaddFaceName_changed(self):
        self.textAddName = self.addFaceName_lineEdit.text().strip()
    def signUpFace(self):
        if self.imgAddName and self.textAddName:
            test = addUser(self.imgAddName,self.textAddName)
            self.blackboard_textEidt.setText(test)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_form = Main_Form()
    main_form.show()
    sys.exit(app.exec_())