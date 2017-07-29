# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from CrawlProject.items import CrawlprojectItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    rules = (
        Rule(LinkExtractor(allow="start=\d+"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
		for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
			item=CrawlprojectItem()
			# 职位名称
			item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
			# 详情连接
			item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
			item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
			item['peopleNum'] =  each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
			item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
			item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]
			
			yield item
			
