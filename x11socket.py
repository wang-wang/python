# -*- coding: utf-8 -*-
#--------vim---------

''' Socket(套接字) 编程是网络编程的一个抽象概念，打开一个Socket需要知道目标计算机的IP地址
和端口号 再指定协议即可
#创建一个socket对象sock = socket.socket(),它的实例化需要3个参数，
1参数 地址家族默认AF_INET(指定使用IPv4协议或者更先进的IPv6 AF_INET6) 或AF_UNIX,
2参数 为面向流的套接字类型(默认socket.SOCK_STREAM,或socket.SOCK_DGRAM)
#3参数 是使用协议(默认是0)

IP地址实际上是一个32位的整数(称为IPv4)以字符串表示的IP地址
如192.168.0.1实际上是把32位整数按8位分组后的数字表示，目的时便于阅读
IPv6地址实际上是一个128位整数 它是目前使用的IPv4的升级版
以字符串表示类似 2001:0db8:85a3:0042:1000:8a2e:0370:7334
'''


#一个小型服务器
import socket

#一个套接字就是一个socket模块中的socket类的一个实例
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#host = socket.gethostname()#得到当前主机名
host = '127.0.0.1'#是一个特殊的IP地址表示本机地址，
#如果绑定到这个地址客户端服务器必须同时在本机运行，也就是说外部的计算机无法连接进来
port = 1234
s.bind((host,port))#使用bind方法将 socket绑定到指定地址和端口(host是主机名port是端口号)

s.listen(5)# 使用listen方法监听端口接收连接请求，参数表示允许排队等待的连接数目，如果队列满就拒绝请求

#在循环中接收发送数据,每个连接都必须创建新线程(或进程)来处理否则单线程在处理连接的过程中，
#无法接受其他客户端的连接
while True:
	c,addr = s.accept()#套接字开始监听后就可以接受客户端的连接这个方法会阻塞(等待)直到客户端连接
						#accept()方法返回包含两个元素的元组(client,address)客户端连接
						#client是客户端套接字 adadress 是客户端地址
	print("Got connectoin from",addr)#Got connectoin from ('127.0.0.1', 43374)
	c.send("Thank you for connecting".encode('utf-8'))#使用send和recv发送和接受数据
	c.close()

'''
python3 新特性对文本和二进制数据作了更为清晰的区分，文本总是Unicode由str类型表示，
二进制数据则由bytes类型表示.
>>>'€20'.encode('utf-8') #字符串编码为字节包
b'\xe2\x82\xac20'

>>>b'\xe2\x82\xac20'.decode('utf-8')# 字节包解码为字符串
'€20'

>>> 'welcome'.encode('utf-8')
b'welcome'

>>>b'welcome.decode('utf-8')
'welcome'

#传入encode和decode的参数是编码，编码是一种用二进制数据表示抽象字符的方式。
####编码是这个转换过程中至关重要的一部分，没有编码bytes对象b\'xa420'只是一堆比特位而已，
####编码赋予其含义，采用不同的编码这些比特位的含义就会大不同

>>> '€20'.encode('iso-8859-15')
b'\xa420'

>>> b'\xa420'.decode('iso-8859-15')
'€20'

>>> b'\xa420'.decode('windows-1255')
'₪20'


'''























