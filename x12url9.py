#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#廖雪峰网站示例
#以POST发送一个请求，只需要把参数data以dbytes形式传入
#模拟一个微波登录 先读取登录的邮箱和口令 然后按照 weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入

from urllib import request ,parse

print('Login to weibo.cn...')
email = input ('Email: ')
passwd = input('Password: ')

login_data = parse.urlencode([('username',email),('password',passwd),('entry','mweibo'),
('client_id',''),('savestate','1'),('ec',''),('pagerefer','https://passport.weibo.cn/sigin/welcome?entry=mweibo&=http%3A%2F%2Fm.weibo.cn%2F')])

req = request.Request('http://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User_Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X)\
AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/853625')

req.add_header('Referer', 'http://passport.weibo.cn/sigin/login?entry=mweibo&res=wel&wm=3349&r=thhp%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
	print('Status:', f.status, f.reason)
	for k,v in f.getheaders():
		print('%s: %s' %(k,v))
print('Data:', f.read().decode('utf-8'))


'''
Status: 200 OK
Server: nginx
Date: Sun, 21 Aug 2016 07:46:03 GMT
.......
DPOOL_HEADER: kotl46
SINA-LB: aGEuNTkuZzEuYngubGIuc2luYW5vZGUuY29t
SINA-TS: ZGZjNGU0Y2UgMCAwIDAgNiA0MAo=
Data: 
'''


print('-----------------------Handler-----------------------------')

#Handler
import urllib
from urllib import request
#通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理


proxy_handler = urllib.request.ProxyHandler({'http:': 'http://www.baidu.com:3128/'})

proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()

proxy_auth_handler.add_password('realm', 'host','username', 'password')

opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.baidu.com/login.html') as f:
	pass

