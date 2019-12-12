import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QFileDialog

from PyQT_Form import Ui_Form
from apitest import test_face

class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)

    # 实现pushButton_click()函数，textEdit是我们放上去的文本框id
    def pushButton_click(self):
        self.textEdit.setText('你点击了按钮')

    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
        self.textEdit.setText(test_face(imgName))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())