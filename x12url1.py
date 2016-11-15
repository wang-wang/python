#!/usr/bin/env python
# -*- coding: utf-8 -*

# 爬取百度贴吧小说吧萝莉正太图片 链接 'http://tieba.baidu.com/p/2127788485'
#储存在 '/home/how/url/url2/' 



from urllib import request
import re

def getHtml(url):
	page = request.urlopen(url)
	html = page.read()
	return html.decode('utf-8')

def getImg(html):
	#reg = r'src="(.+?\.jpg)"'
	reg = r'src="(.*?\.jpg)" pic_ext'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	path = '/home/how/url/url2/'
	x = 0
	for imgurl in imglist:
		request.urlretrieve(imgurl,'%s %d' %(path,x))
		x += 1


if __name__ == '__main__':
	html = getHtml('http://tieba.baidu.com/p/2127788485')
	getImg(html)

