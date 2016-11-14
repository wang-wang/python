# -*- coding: utf-8 -*-
#------vim------

#接收 x11socket5.py 客户机

import socket 
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8001))

time.sleep(3)
# encode('utf-8')将字符串编码为字节包
#sock.send('1')原例
sock.send(('2').encode('utf-8'))

print(sock.recv(1024))
sock.close()

