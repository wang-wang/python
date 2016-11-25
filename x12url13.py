#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#慕课网示例
#爬取百度百科Python词条相关1000个页面数据
#python 2


import x12url12
from bs4 import BeautifulSoup

class SpiderMain(object):

	def __init__(self):
		self.urls = x12url12.UrlManager()# 管理
		self.downloader = x12url12.HtmlDownloader()#下载
		self.parser = x12url12.HtmlParser()#解析
		self.outputer = x12url12.HtmlOutputer()#输出

	def craw(self,root_url):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print('craw %d : %s' %(count, new_url))
				html_cont = self.downloader.download(new_url)
				new_urls, new_data = self.parser.parse(new_url, html_cont)
				self.urls.add_new_urls(new_urls)
				self.outputer.collect_data(new_data)
			
				if count == 1000:
					break		
			
				count += 1
			except Exception as e :
				print('craw failed: ',e)
		self.outputer.output_html()		
			





if __name__ == '__main__':
	root_url = 'http://baike.baidu.com/view/21087.htm'
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)



