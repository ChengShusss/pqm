"""
Description: 

Author: Cheng Shu
Date: 2021-11-10 09:02:39
LastEditTime: 2021-11-10 09:03:47
LastEditors: Cheng Shu
@Copyright © 2020 Cheng Shu
License: MIT License
"""


import serial #导入模块
import serial.tools.list_ports


port_list = list(serial.tools.list_ports.comports())
ports = []
for port in port_list:
    name = port.name
    desc = port.description[:port.description.find(' ')]
    ports.append([name, desc])
print(ports)