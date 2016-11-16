#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#抓取ZOL桌面壁纸电脑壁纸 
#url http://desk.zol.com.cn/pc/
from urllib import request
from bs4 import BeautifulSoup as bs
import re ,random 
import os, os.path


#得到网站soup对象
def get_soup(url):
	myheaders = [
	'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
	'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
	'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
	'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
	'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36']
	print(111111111111)
	header = {'User-Agent':random.choice(myheaders)}
	req = request.Request(url,headers=header)
	html = request.urlopen(req).read()
	soup = bs(html,'html.parser',from_encoding='utf-8')
	#print(soup)
	return soup

#获取图片标题
def get_title(url):
	print(22222222222222222222222)
	soup = get_soup(url)
	title = soup.find_all('a',class_="pic")
	#print('title', title)
	names = []
	for ti in title:
		for i in ti:
			result = i.get('alt')
			names.append(result)
	names = set(names)
	return list(names)
#['弹珠简约高清桌面壁纸', '', '昆塔之盒子总动员动漫壁纸', '在那桃花盛开的地方', '唯美花朵桌面壁纸', '孢子计划桌面壁纸-孢子菌','''

#获取图片
def get_image(url,filename):
	print(33333333333333333333)
	soup = get_soup(url)
	#print(soup.prettify())
	img = soup.find_all('img')[1]['src']#img http://desk.fd.zol-img.com.cn/t_s208x130c5/g5/M00/0F/02/ChMkJlfIBA2IK4BUAAg4NDai3KUAAU50AET9doACDhM284.jpg
	print('img',img)
	request.urlretrieve(img,filename)




#开始下载图片
def main():
	print(4444444444444444444444444444444444444)
	for i in names:
		print('********主题 %s ×××××××××××' % i)
		for i in range(1,50):# 50张图片
			pic_url = url+str(i)+'.html'
			print(pic_url)
			get_image(pic_url,'{}{}'.format(filename,i))


		

if __name__ == '__main__':
	url ='http://desk.zol.com.cn/pc/'
	filename = '/home/how/url/url8/'
	#get_image(url,filename)
	names = get_title(url)
	print(names)
	main()










