# -*_ coding: utf-8 -*-
#--------vim-------

#向x11xocket6.py发送消息
# socket服务器例子

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',8001))
sock.listen(5)
	
while True:
	connection,address = sock.accept()
	try:
		connection.settimeout(5)# 超过5秒就抛出socket.timeout错误
		buf = connection.recv(1024)# 接受来自客户端的数据
		#if buf == '1':原例
		if buf == '1'.encode('utf-8'):
			connection.send(('welcome to sever!').encode('utf-8'))
		else:
			connection.send(('please go out!').encode('utf-8'))
	except socket.timeout:
		print("time out")
	connection.close()
	
