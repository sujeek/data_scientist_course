# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from w3schooldemo.items import W3SchooldemoItem
 
class W3schoolSpider(Spider):
	name = 'w3schooldemo'
	allowed_domains = ["w3school.com.cn"]
	start_urls = ['http://www.w3school.com.cn/']
 
	def parse(self,response):
		sel = Selector(response)
		sites = sel.xpath('//div[@id="navfirst"]/ul[1]/li')#找到id=navfirst的div，找到其中ul里面li里的信息。
		items = []
 
		for site in sites:
			item = W3SchooldemoItem()#每个item都相当于一个字典
 
			title = site.xpath('a/text()').extract()#提取<a></a>中间的内容
			link = site.xpath('a/@href').extract()#提取<a>中href的内容
			desc = site.xpath('a/@title').extract()#提取<a>中title的内容
 
			item['title'] = [t for t in title]
			item['link'] = [l for l in link]
			item['desc'] = [d for d in desc]
 
			items.append(item)
		return items