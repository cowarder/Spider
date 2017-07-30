# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from DongGuan.items import DongguanItem


class DongguanSpider(CrawlSpider):
	name = 'dongguan'
	allowed_domains = ['wz.sun0769.com']
	start_urls = ['http://wz.sun0769.com/index.php/question/report?page=0']

	rules=(
	Rule(LinkExtractor(allow=r'page=\d+')),
	Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'), callback='parse_item', follow=False)
	)

	def parse_item(self, response):
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
		print response.url
		for each in response.xpath('//div[@class="pagecenter p3"]'):
			item=DongguanItem()
			item["title"]=each.xpath(".//strong[@class='tgray14']/text()").extract()[0]

			item["num"]=item["title"].split(" ")[-1].split(":")[-1]
			
			item["content"]=each.xpath(".//div[@class='c1 text14_2']/text()").extract()[0]
			print "666666"
			
			yield item
			
