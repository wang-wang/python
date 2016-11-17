#!/usr/bin/env python
# -*- coding: utf-8 -*-

#原例 Crossin 编程教室

from urllib import request
import json


web = request.urlopen(r'http://www.baidu.com')
page = web.read()

#print(page.decode('utf-8'))
#print(page)
#with open('/home/how/test1/t14python.html', 'wb') as f:
#	f.write(page)

#抓取省份列表

url1 = 'http://m.weather.com.cn/data5/city.xml'
content1 = request.urlopen(url1).read()
content1 = content1.decode('utf-8')
provinces = content1.split(',')
#print(content1)# 01|北京,02|上海,03|天津,04|重庆,05|黑龙江,
#print(provinces)# ['01|北京', '02|上海', '03|天津', '04|重庆', '05|黑龙江',

#对于每个省 抓取城市列表
url2 = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
	p_code = p.split('|')[0]
	url21 = url2%p_code
	content2 = request.urlopen(url21).read()
	content2 = content2.decode('utf-8')
	cities = content2.split(',')

	print(content2)# 0101|北京0201|上海0301|天津3401|台北,3402|高雄,3403|台中
	#print(cities)# ['0101|北京']['0201|上海']['3401|台北', '3402|高雄', '3403|台中']

#对于每个城市 抓取地区列表

for c in cities[:3]:
	c_code = c.split('|')[0]
	url3 = url2%c_code
	content3 = request.urlopen(url3).read()
	content3 = content3.decode('utf-8')
	districts = content3.split(',')
	print(content3)# 340101|台北县
	print(districts)# ['340101|台北县']

#对于每个地区，把名字记录下来再发送一次请求 得到它的最终代码
for d in districts:
	d_pair = d.split('|')
	d_code = d_pair[0]
	name = d_pair[1]
	url4 = url2%d_code
	content4 = request.urlopen(url4).read()
	content4 = content4.decode('utf-8')
	code = content4.split('|')[1]
	line = '%s : %s' %(name,code)
	print(line) #台中 : 101340401


'''


from urllib import request
import json

url1 = 'http://m.weather.com.cn/data5/city.xml'

content1 = request.urlopen(url1).read()
content1 = content1.decode('utf-8')
provinces = content1.split(',')
result = 'city = {\n'
url =' http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
	p_code = p.split('|')[0]
	url2 = url%p_code
	content2 = request.urlopen(url2).read()
	content2 = content2.decode('utf-8')
	cities = content2.split(',')
	for c in cities:
		c_code = c.split('|')[0]
		url3 = url%c_code
		content3 = request.urlopen(url3).read()
		content3 = content3.decode('utf-8')
		districts = content3.split(',')
		for d in districts:
			d_pair = d.split('|')
			d_code = d_pair[0]
			name = d_pair[1]
			url4 = url%d_code
			content4 = request.urlopen(url4).read()
			content4 = content4.decode('utf-8')
			code = content4.split('|')[0]
			line = "  ' %s' : '%s' , \n" %(name,code)
			result += line
			if code:
				pass
			print(name + ':' + '101'+code)
result += '}'
with open('/home/how/pythont/url_city.py', 'w') as f:
	f.write(result)



# code = content4.split('|')[0]原例子为code = content4.split('|')[1]
#显示IndexError: list index out of range错误  name松江 的对应 code号码没有解析出来'''

'''
print(content4, name>>>/)
<html>
<head>
</head>
<body>
<script type="text/javascript">
	window.onload = function() {
	window.open("/","_self");
	}; 
	</script> 
 <!-- START WRating v1.0 -->
<script type="text/javascript" src="http://c.wrating.com/a1.js">
</script>
<script type="text/javascript">
var vjAcc="860010-2151010100";
var wrUrl="http://c.wrating.com/";
vjTrack("");
</script>
<noscript><img src="http://c.wrating.com/a.gif?a=&c=860010-2151010100" width="1" height="1"/></noscript>
<!-- END WRating v1.0 -->
</body>
</html>
 松江 >>>/
Traceback (most recent call last):
  File "/home/how/python1/x12url6.py", line 34, in <module>
    code = content4.split('|')[1]
IndexError: list index out of range
'''
