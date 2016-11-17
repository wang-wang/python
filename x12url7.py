#!/usr/bin/env python
# -*- coding: utf-8 -*-

#原例 Crossin编程教室

from urllib import request 
from city import city
import json # json(JaveScript Object Notation)是一种轻量级的数据交换格式，易于人阅读和编写同时也易于机器解析和生成
#编码 把一个Python对象编码转换成Json字符串 json.dumps()
#解码 把Json格式字符串解码转换成Python对象 json.loads()

cityname = input('你想查哪个城市的天气？\n')
citycode = city.get(cityname)
if citycode:
	try:
		url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
		content = request.urlopen(url).read()
		#print('11',content)
		#print(type(content))# <class 'bytes'>
		content = content.decode('utf-8')
		#print('22',content)
		#print(type(content))# <class 'str'>
		data = json.loads(content)#将满足json格式的字符串转换成一个真正的字典
		#print('data',data)
		#print(type(data))#<class 'dict'>
		result = data['weatherinfo']
		str_temp = ('%s\n%s ~ %s') %(
				result['weather'],
				result['temp1'],
				result['temp2']
		)
		print(str_temp)
	except Exception as e:
		print('Error 查存失败:',e)
else:
	print('没有找到该城市')

'''
你想查哪个城市的天气？
北京
11 b'{"weatherinfo":{"city":"\xe5\x8c\x97\xe4\xba\xac","cityid":"101010100","temp1":"-2\xe2\x84\x83","temp2":"16\xe2\x84\x83","weather":"\xe6\x99\xb4","img1":"n0.gif","img2":"d0.gif","ptime":"18:00"}}'
22 {"weatherinfo":{"city":"北京","cityid":"101010100","temp1":"-2℃","temp2":"16℃","weather":"晴","img1":"n0.gif","img2":"d0.gif","ptime":"18:00"}}
data {'weatherinfo': {'city': '北京', 'temp2': '16℃', 'cityid': '101010100', 'img1': 'n0.gif', 'ptime': '18:00', 'weather': '晴', 'img2': 'd0.gif', 'temp1': '-2℃'}}
晴
-2℃ ~ 16℃
'''











