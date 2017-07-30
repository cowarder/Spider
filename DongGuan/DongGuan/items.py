# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #提问标题
	title=scrapy.Field()
	#问题编号
	num=scrapy.Field()
	#问题内容
	content=scrapy.Field()
	
