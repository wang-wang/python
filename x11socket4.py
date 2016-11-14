# -*- coding: utf-8 -*-
#--------vim-------
#接收x11socket3.py -客户端


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1',9999))

#接收欢迎消息
print(s.recv(1024).decode('utf-8'))

for data in [b'Micheal',b'Tracy',b'Sarah']:
	s.send(data)#发送数据
	print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()

