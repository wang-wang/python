#!/usr/bin/env python
# -*- coding: utf-8 -*-
 

#廖雪峰网站示例
#python3 发送一个 get请求到指定页面 然后返回HTTP的响应
 
from urllib import request
 
with request .urlopen('http://api.douban.com/v2/book/2129650') as f:
	data = f.read()
	print("Status:", f.status,f.reason)
	for k,v in f.getheaders():
		print('%s: %s' %(k,v))
	print('Data:',data.decode('utf-8'))

#返回的HTTP响应的头和JSON数据
'''
Status: 200 OK
Server: nginx
Date: Tue, 26 May 2015 10:02:27 GMT
Content-Type: application/json; charset=utf-8
Data: {"rating":{"max":10,"numRaters":16,"average":"7.4","min":0},"subtitle":"","author":["廖雪峰编著"],"pubdate":"2007-6"....
'''

#模拟浏览器发送 GET 请求，通过往Request对象添加HTTP头就可以把请求伪装成浏览器
#模拟iPhone 6去请求豆瓣首页

req = request.Request('http://www.ddouban.com/')
req.add_header('User-Agent', 'Mozilla/6.0(iPhone; CPU iPhone OS 8_0 like Mac OS X) \
AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
	print("Sratus:", f.status, f.reason)
	for k,v in f.getgeaders():
		print('%s: %s' %(k,v))
	print('Data:', f.read().decode('utf-8'))


#豆瓣会返回适合 iPhone 的移动版网页
'''
<meta charset="UTF-8">
        <title>豆瓣(手机版)</title>
        <meta name="viewport" content="width=device-width, height=device-height, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0">
        <meta name="format-detection" content="telephone=no">
        <link rel="canonical" href="https://m.douban.com/">
        <link href="https://img3.doubanio.com/f/talion/038e67eae4b0acf975bd3803a99d28649c8db7ac/css/card/base.css" rel="stylesheet">
        
'''

