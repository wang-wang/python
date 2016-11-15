#!/usr/bin/env python
# -*- coding: utf-8 -*-


#爬取糗事百科热门段子 参照原例 伯乐在线 Python爬虫实战（1）：爬取糗事百科段子
#http://python.jobbole.com/81351/

import re
from urllib import request
from bs4 import BeautifulSoup as bs

headers= 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36'
page = 1
url = 'http://www.qiushibaike.com/hot/'

class QSBK():
#初始化
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36'
		self.headers = {'User-Agent': self.user_agent}
		self.stories = []
		self.enable = True
#得到页面 soup
	def get_page(self,pageIndex):
		try:
			url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
			print(url)
			req = request.Request(url,headers = self.headers)
			resp = request.urlopen(req).read()
			soup = bs(resp,'html.parser')
			return soup
		except request.URLError as e:
			print('连接糗事百科失败 错误原因',e)
			return None
	
#获取页面内容
	def get_pageitems(self,pageIndex):
		pageSoup = 	self.get_page(pageIndex)
		if not pageSoup:
			print('页面加载失败。。。')
			return None
		div = pageSoup.find_all('div',class_='article block untagged mb15')
		for i in range(0,20):
			Publisher= div[i]#发布人内容
			Publisher_Name = Publisher.find('img')['alt']# 发布人名称
			Head_portrait = Publisher.find('img')['src'] #发布人头像
			Post_content = Publisher.find('div',class_='content') # 发布内容 
			Funny_comments= Publisher.find_all('i') #好笑数 评论数
			print('发布人名称：%s\n 发布人头像: %s\n 发布内容:%s\n 好笑数:%s\n 评论数: %s' %(Publisher_Name,Head_portrait,str(Post_content).strip('<div class="content> </div>'), str(Funny_comments[0]).strip('<i class="number"> </i>'), str(Funny_comments[1]).strip('<i class="number"></i>')))
			
		#content2 = content1.find('img')['alt']# 发布人名称
		#content3 = content1.find('img')['src'] #发布人头像
		#content4 = content1.find('div',class_='content') # 发布内容 # find_all(class_='content')
		#content5 = content1.find_all('i') #好笑数 评论数

		#items = pageSoup.find_all('div',class_="content") #段子内容
		#items0 = pageSoup.find_all('a',target = '_blank')[0].find_all('img')[0]['alt']#获取发布人
		#items1 = pageSoup.find_all('a',target = '_blank')[2].find_all('i')[0]# 评论
		#items2 = pageSoup.find_all('i',class_="number") #好笑

		#print('items',items[0])
		#print('items0',items0)#[0]['alt'])#发布人  #items0 污林～忘忘
		#print('items1',items1) # 评论 #items1 <i class="number">299</i>
		#print('items2',items2[0]) #好笑 #items2 <i class="number">15811</i>
		#print(div)
		#print('content1',content1) ##第一个发布人内容
		#print('content2', content2) ## 发布人名称
		#print('content3', content3) #发布人头像
		#print('content4', content4) # 发布内容
		#print('content4', str(content4).strip('<div class="content> </div>'))  # 发布内容
		#print('content5', content5, '好笑',content5[0],'评论',content5[1])#好笑数 评论数
		#print('content5', '好笑', str(content5[0]).strip('<i class="number"> </i>'))  # 好笑数
		#print('content5','评论', str(content5[1]).strip('<i class="number"></i>'))#评论数
		#print(pageSoup)

#开始
	def start(self):
		print('读取糗事百科段子')
		page_start = input('Input the first page number: \n')
		page_end = input('Input the last page number: \n')
		if page_start and page_end == 'Q':
			self.enable = False
		for page in range(int(page_start),int(page_end)):
			self.get_pageitems(page)



spider = QSBK()
spider.start()








