import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QFileDialog

from apitest import test_face
from IndexUI import Ui_TabWidget

class Main_Form(QtWidgets.QTabWidget,Ui_TabWidget):
    def __init__(self):
        super(Main_Form,self).__init__()
        self.setupUi(self)

    def chooseFace(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.faceIdentification_label.width(), self.faceIdentification_label.height())
        self.faceIdentification_label.setPixmap(jpg)
        self.clockInRecordsList.addItem(test_face(imgName))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_form = Main_Form()
    main_form.show()
    sys.exit(app.exec_())