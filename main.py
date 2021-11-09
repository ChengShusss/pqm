#encoding=utf-8
"""
Description: 

Author: Cheng Shu
Date: 2021-11-09 21:32:15
LastEditTime: 2021-11-09 23:02:45
LastEditors: Cheng Shu
@Copyright © 2020 Cheng Shu
License: MIT License
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
# from dialog import Ui_Dialog
from mainWindow import Ui_MainWindow
from functools import partial

import serial #导入模块

import serial.tools.list_ports


def convert(ui):
    try:
        input = ui.inputEdit.text()
        result = float(input) * 6.7
        ui.outputEdit.setText(str(result))
    except ValueError as e:
        QMessageBox.warning(ui, "警告", "输入值不合法",QMessageBox.Yes ,QMessageBox.Yes)
    finally:
        return
        


class MyDesiger(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyDesiger, self).__init__(parent)
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.onClick)
        self.btn_transform.clicked.connect(partial(convert, self))
        self.btn_portScan.clicked.connect(self.scan)

    def scan(self):
        port_list = list(serial.tools.list_ports.comports())
        # print(port_list)
        if len(port_list) == 0:
            print('无可用串口')
        else:
            ports = []
            for port in port_list:
                name = port.name
                desc = port.description[:port.description.find(' ')]
                ports.append([name, desc])
            print(ports)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MyDesiger()
    ui.show()
    sys.exit(app.exec_())