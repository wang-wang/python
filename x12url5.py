#!/usr/bin/env python
# -*- coding: utf-8 -*-


#爬取百度贴吧桌面吧图片  
#贴吧链接'http://tieba.baidu.com/p/2460150866?pn='

import urllib, urllib.request
import re, os


def getHtml(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	
	return html.decode('utf-8')

def getImg(html):
	reg = r'src="(http://.+?\.jpg)" pic_ext' #reg = r'src="(.+?\.jpg)" pic_ext'
	imgre = re.compile(reg)
	imglist = imgre.findall(html)
	x = 0
	
	path = '/home/how/url/url6/'
	if not os.path.isdir(path):
		os.makedirs(path)
	for imgurl in imglist:
		urllib.request.urlretrieve(imgurl,'{}{}={}.jpg'.format(path,pa,x))
		x = x +1
		print(x)

for pa in range(1,75):
	try:# 出现HTTP未找到错误 Error: HTTP Error 404: Not Found

		url = 'http://tieba.baidu.com/p/2460150866?pn='
		urls = url + str(pa)
		print(urls)
		html = getHtml(urls)
		getImg(html)
	except Exception as e:
		print('Error:', e)


