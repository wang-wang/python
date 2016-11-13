# -*- coding: utf-8 -*-
#--------vim--------
# 服务器 接收 x11socket4.py

import socket
import time
import threading #threading 通过对thread模块进行二次封装，提供了api来处理线程
#thread模块以低级 原始的方式来处理和控制线程

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#监听端口
s.bind(('127.0.0.1',9999))
s.listen(5)
print("Waiting for connecting......")

 
def tcplink(sock,addr):
	print("Accept new connection from %s:%s..." %addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(("Hello, %s!" %data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print("Connection from %s:%s closed." %addr)


#循环接受来自客户端的连接
while True:
	sock, addr = s.accept()#创建一个新连接
	t = threading.Thread(target=tcplink, args=(sock,addr))#创建新线程来处理TCP连接
	t.start()
