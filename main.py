#encoding=utf-8
"""
Description: 

Author: Cheng Shu
Date: 2021-11-09 21:32:15
LastEditTime: 2021-11-09 23:49:19
LastEditors: Cheng Shu
@Copyright © 2020 Cheng Shu
License: MIT License
"""
import sys
from PyQt5 import QtCore, QtWidgets

import matplotlib
matplotlib.use('Qt5Agg')
# 使用 matplotlib中的FigureCanvas (在使用 Qt5 Backends中 FigureCanvas继承自QtWidgets.QWidget)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import serial #导入模块
import serial.tools.list_ports
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
# from dialog import Ui_Dialog
from mainWindow import Ui_MainWindow
import numpy as np


class MyMatplotlibFigure(FigureCanvas):
    """
    创建一个画布类，并把画布放到FigureCanvasQTAgg
    """
    def __init__(self, width=3, heigh=3, dpi=100):
        plt.rcParams['figure.facecolor'] = 'r'  # 设置窗体颜色
        plt.rcParams['axes.facecolor'] = 'b'  # 设置绘图区颜色
        # 创建一个Figure,该Figure为matplotlib下的Figure，不是matplotlib.pyplot下面的Figure
        # 这里还要注意，width, heigh可以直接调用参数，不能用self.width、self.heigh作为变量获取，因为self.width、self.heigh 在模块中已经FigureCanvasQTAgg模块中使用，这里定义会造成覆盖
        self.figs = Figure(figsize=(width, heigh), dpi=dpi)
        super(MyMatplotlibFigure, self).__init__(self.figs)  # 在父类种激活self.fig， 否则不能显示图像（就是在画板上放置画布）
        self.axes = self.figs.add_subplot(111)  # 添加绘图区


class MyDesiger(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyDesiger, self).__init__(parent)
        self.setupUi(self)
        self.btn_portScan.clicked.connect(self.scan)
        # self.widget.add
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(5, 20, 400, 200))
        self.canvas = MyMatplotlibFigure(width=2, heigh=2, dpi=100)
        self.plotcos()
        self.hboxlayout = QtWidgets.QHBoxLayout(self.label)
        self.hboxlayout.addWidget(self.canvas)

    def scan(self):
        """
        扫描端口，更新列表
        """
        port_list = list(serial.tools.list_ports.comports())
        selected = self.box_ports.currentText()
        self.box_ports.clear()
        if len(port_list) == 0:
            # 若串口列表为空，提示
            QMessageBox.information(ui, "提示", "无可用串口",QMessageBox.Yes ,QMessageBox.Yes)
        else:
            # 更新串口信息
            ports = []
            for port in port_list:
                name = port.name
                desc = port.description[:port.description.find(' ')]
                ports.append([name, desc])
            # 更新列表数据
            texts = [x[0] for x in ports]
            self.box_ports.addItems(texts)
            if selected in texts:
                # 恢复刷新前所选择的串口
                self.box_ports.setCurrentIndex(texts.index(selected))

    def plotcos(self):
        # plt.clf()
        t = np.arange(0.0, 5.0, 0.01)
        s = np.cos(2 * np.pi * t)
        self.canvas.axes.plot(t, s)
        self.canvas.figs.suptitle("sin")  # 设置标题
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MyDesiger()
    ui.show()
    sys.exit(app.exec_())