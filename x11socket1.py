# -*- coding: utf-8 -*-
#--------vim---------
''' Socket 编程是网络编程的一个抽象概念，打开一个Socket需要知道目标计算机的IP地址
和端口号 再指定协议即可

'''

#一个小型客户机

#导入socket库
import socket

#创建一个socket对象sock = socket.socket(),它的实例化需要3个参数，1地址家族默认AF_INET(指定使用IPv4协议
#或者更先进的IPv6 AF_INET6) 或AF_UNIX,2参数为 面向流的套接字类型(默认socket.SOCK_STREAM,或socket.SOCK_DGRAM)
#3参数是使用协议(默认时0)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host = socket.gethostname()
host = '127.0.0.1'
port = 1234

s.connect((host,port))

print(s.recv(1024))
# 
