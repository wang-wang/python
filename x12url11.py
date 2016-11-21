#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#抓取全智贤百度贴吧图片 储存在 '/home/how/url/url5/'
# 原例连接 http://blog.csdn.net/z49434574/article/details/51552088
# 贴吧连接 http://tieba.baidu.com/p/3466236659?pn=1

import re
from urllib import request


def gethtml(url):
	page = request.urlopen(url)
	html = page.read()
	return html.decode('utf-8')


def getimg(html):
	x =1
	reg = 'src="(http://img.+?\.jpg)"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	path = '/home/how/url/url5/'
	for img in imglist:
		print(x)
		request.urlretrieve(img,'%s %d-%d.jpg' %(path,k,x))
		x += 1

if __name__ == '__main__':
	url = 'http://tieba.baidu.com/p/3466236659?pn='
	for k in range(1,29):	
		urls = url+str(k)
		print(urls)
		html = gethtml(urls)
		getimg(html)
