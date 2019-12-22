'''这个例子中不使用面向对象的方式，而是使用面向过程的方式'''
import sys  # 获取参数的api
import cv2 as cv
import numpy as np
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QApplication, QWidget, QPushButton  # 因为需要创建主窗口和应用程序


def video_demo():
    # 0是代表摄像头编号，只有一个的话默认为0
    capture = cv.VideoCapture(0)
    while (True):
        ref, frame = capture.read()
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        # 变换彩色空间顺序
        cv.cvtColor(frame, cv.COLOR_BGR2RGB, frame)
        # 转为QImage对象
        image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
        # self.view.setPixmap(QPixmap.fromImage(self.image))
        cv.imshow("1", frame)
        # 等待30ms显示图像，若过程中按“Esc”退出
        c = cv.waitKey(30) & 0xff
        if c == 27:
            capture.release()
            break
    cv.waitKey(0)


# 不是使用类了，直接使用
app = QApplication(sys.argv)

widget = QWidget()  # d定义一个窗口
btn = QPushButton(widget)
btn.setText("打开图片")  # 按钮名称
btn.clicked.connect(video_demo)  # 如果点击的话会连接到onClick_Button

btn.move(24, 53)  # 按钮坐标位置,越高坐标越小左上角为（0，0）

widget.resize(300, 240)  # 窗口大小(其实是设置工作区的)

widget.move(250, 200)

widget.setWindowTitle("简单窗口")  # 窗口标题

widget.show()

sys.exit(app.exec_())#不加这句话的后果是窗口直接一闪而过


