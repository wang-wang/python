#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#抓取妹子图网站图片 
#原例来源 玩蛇网来源网址：http://www.iplaypython.com/crawler/250.html

from bs4 import BeautifulSoup
from urllib import request
import os,os.path
import random

#获取网站的soup对象
def get_soup(url):
	print('111111111111111111111111111111111111')
	my_headers = [
	'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
	'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
	'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
	'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
	'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36']
	random_Mozilla = random.choice(my_headers)
	header = {'User-Agent':random_Mozilla}
	req = request.Request(url,headers=header)
	html = request.urlopen(req).read()#.decode('utf-8')
	soup = BeautifulSoup(html)
	return soup

#获取图片网站页数
def get_pages(url):
	print('22222222222222222222222222222222222222')
	soup = get_soup(url)
	nums = soup.find_all('a',class_='page-numbers')
	pages = int(nums[-2].text)
	return pages

#获取页面所有妹子图主题的连接名和地址记入列表
def get_menu(url):
	print('3333333333333333333333333333333333')
	soup = get_soup(url)
	menu = []
	menu_list = soup.find_all('a',target='_blank')
	for i in menu_list:
		result = i.find_all('img',class_='lazy')
		if result:
			name = result[0]['alt']
			address = i['href']
			menu.append([name,address])
	return menu

#获取单个妹子图主题一共有多少图片
def get_links(url):
	print('4444444444444444444444444444444444444')
	soup = get_soup(url)
	all = soup.find_all('a')
	nums = []
	for i in all:
		span = i.find_all('span')
		if span:
			nums.append(span[0].text)
	return nums[-2]

#从单独的页面中提取图片保存为 filename
def get_image(url,filename):
	print('555555555555555555555555555555555555')
	soup = get_soup(url)
	image = soup.find_all('p')[0].find_all('img')[0]['src']
	request.urlretrieve(image,filename)

#下载page页的妹子图
def main(page):
	print('6666666666666666666666666666666666')
	print('正在下载第 %d 页' % page)
	page_url = url+'/page/'+str(page)
	menu = get_menu(page_url)
	print(u'@@@@@@@@@@@@@@@@第 %d 页共有 %d 个主题@@@@@@@@@@@@@@@@' %(page,len(menu)))
	for i in menu:
		print(i,'>>>>>>>>>>>>>>>iiii')
		dir_name = os.path.join('/home/how/url/url7mzt',i[0])
		if not os.path.exists(dir_name):#os.path.exists(指定路径是否存在)
			os.mkdir(dir_name)
		pic_nums = int(get_links(i[1]))
		print( u'\n\n\n*******主题 %s 一共有 %d 张图片******\n' %(i[0],pic_nums))
		for pic in range(1,pic_nums+1):
			basename = str(pic) + '.jpg'
			filename = os.path.join(dir_name,basename)
			pic_url = i[1]+'/'+str(pic)
			if not os.path.exists(filename):
				print(u'.......%s' %basename)
				get_image(pic_url,filename)
			else:
				print(filename+u'已存在 ，略过')


if __name__ == '__main__':
	print('77777777777777777777777777777777777777')
	url = 'http://www.mzitu.com/'
	pages = get_pages(url)
	print(u'********************妹子图一共有 %d 页××××××××××××××××××' %pages)
	if not os.path.exists('/home/how/url/url7mzt/'):
		os.mkdir('/home/how/url/url7mzt/')
	page_start = input(u'Input the frist page number: \n')
	page_end = input(u'Input the last page number: \n')
	if page_end > page_start:
		for page in range(page_start,page_end):
			main(int(page))
	elif page_end == page_start:
		main(int(page_end))
	else:
		print(u'输入错误，起始页必须小于等于结束页\n')



