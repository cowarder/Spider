# -*- coding: utf-8 -*-
import scrapy
from DouBan.items import DoubanItem


class DoubanSpider(scrapy.Spider):
	name = 'douban'
	allowed_domains = ['movie.douban.com']
	offset=0
	url="https://movie.douban.com/top250?start="
	start_urls = [url+str(offset)]

	def parse(self, response):
		for each in response.xpath('//div//ol[@class="grid_view"]/li'):
			item=DoubanItem()
			item["name"]=each.xpath('.//span[@class="title"][1]/text()').extract()[0]
			 
			des=each.xpath('.//span[@class="inq"]/text()').extract()
			if len(des) >0:
				item["description"]=des
				
			item["point"]=each.xpath('.//span[@class="rating_num"]/text()').extract()[0]
			yield item
			
		
		self.offset+=25
		
		if self.offset <= 225:
			yield scrapy.Request(self.url+str(self.offset),callback=self.parse)
		
		
