# -*- coding: utf-8 -*-
#--------vim---------
#廖雪峰客户端示例 获取新浪首页

import socket #导入socket库

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('www.sina.com',80))

#发送数据
s.send(b'GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接受数据

buffer = []

while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)

s.close()#关闭连接

header, html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
#把接收的数据写入文件
print('---------------------')
with open('/home/how/test1/t12sina.html','wb') as f:
	f.write(html)






