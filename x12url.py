#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python3

'''

import urllib
import  re
from urllib import request

url = 'http://image.baidu.com'

#模拟真实浏览器 携带 User-Agent头
req = request.Request(url)
#req.add_header(key,value)
req.add_header('User-Agent','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36')

resp = request.urlopen(req)
print(resp.read().decode('utf-8'))

print('--------------------python3 读取网页--------------')

import urllib.request
from urllib import parse
response = urllib.request.urlopen("http://acm.hit.edu.cn")
html = response.read()
z_data = html.decode('utf-8')#转码后看见原来的字符如汉字，如果不对试一试 'GBK'解码
#print(z_data)

file1 = open('/home/how/url/url1.txt','wb')# python是types格式，得用二进制读写
file1.write(html)
file1.close()

data = {}
data['key'] = 'python3'
url_values = urllib.parse.urlencode(data)# 结果为python3
url = 'http://www.baidu.com/s?'
full_url = url+url_values
print(full_url) #得到的url为 :http://www.baidu.com/s?key=python3

# 根据HTML 网页字符串创建BeautifulSoup对象
#suop = BEautifulSoup(html_doc(HTML文档字符串），'html.parser'(HTML解析器),
#from_encoding='utf-8'(HTML文档的编码))
'''
print('----------------------使用 POST请求-------------------------')

from urllib.request import urlopen
from urllib.request import Request
from urllib import parse
#使用urlencode生成post数据
#postData = parse.urlencode([(key1,val1),(key1,val2),(keyn,valn)])
# 使用postData发送post请求 #request.urlopen(req,data=postData.encode('utf-8'))
#得到请求状态 #resp.status
#得到服务器的类型 #resq.reason

reqs = Request('http://www.thsrc.com.tw/tw/TimeTable/SearchResult')

postData = parse.urlencode([
	('StartStation','977abb69-413a-4ccf-a109-0272c24fd490'),
	('EndStation','9c5ac6ca-ec89-48f8-aab0-41b738cb1814'),
	('SearchDate','2016/08/27'),
	('SearchTime','15:30'),
	('SearchWay','DepartureInMandarin')
])
#添加多个头 reqs.add_header()
reqs.add_header('Origin','http//www.thsrc.com.tw')#来源
reqs.add_header('User-Agent','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36')#模拟浏览器头
resps = urlopen(reqs, data = postData.encode('utf-8'))

print(resps.read().decode('utf-8'))



