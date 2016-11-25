#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
SocketServer 简话了网络服务器的编写同时也是python标准库中很多服务器框架的基础
Socketserver模块提供请求处理类有BaseRequestHandler以及它的派生类
StreamRequestHandler(处理流式套接字)和DatagramRequestHandler(处理数据报套接字)
事件驱动 只有事件出现的时候(有客户端连接)程序才会有反应


'''

# x13socketserver1.py的服务器
from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)

from time import ctime

host = '127.0.0.1'
port = 1311
addr = (host,port)

#创建请求处理类 继承BaseRequestandler并重写它的handle()方法
class MyRequestHandler(SRH):
	def handle(self):
		print('.......connected from:', self.client_address[0])
		self.data = self.request.recv(1024).strip()#接收客户端的消息
		print('---self.data---',self.data)
		self.wfile.write(('%s $$ %s' %('socketserver',self.data.decode('utf-8'))).encode('utf-8'))#向客户端发送消息

		time = ctime().encode('utf-8')
		self.wfile.write(('\nconnection %s: %s at %s succeed!' %(host,port,ctime())).encode('utf-8')) 

tcpServ = TCP(addr,MyRequestHandler)#实例化一个服务器类对象
print('waiting forconnection...')
tcpServ.serve_forever()#调用服务类对象的 handle_request() 或 serve_forever()方法来开始处理请求
#tcpServ.handle_request()客户端连接后关闭后 关闭tcpServ



