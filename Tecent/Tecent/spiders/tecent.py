# -*- coding: utf-8 -*-
import scrapy
import json
from Tecent.items import TecentItem

class TecentSpider(scrapy.Spider):
    name = 'tecent'
    allowed_domains = ['tencent.com']
    page=0
    url='http://hr.tencent.com/position.php?&start='
    start_urls = [url+str(page)]


    def parse(self, response):
    	with open("job.html","w") as f:
    		f.write(response.body)
    	job_list=response.xpath("//tr[@class='even']|//tr[@class='odd']")

    	#ItemList=[]
    	for item in job_list:
    		Item=TecentItem()
    		jobName=item.xpath("./td[1]/a/text()").extract()[0]
    		jobLink=item.xpath("./td[1]/a/@href").extract()[0]
    		jobType=item.xpath("./td[2]/text()").extract()[0]
    		recruitNum=item.xpath("./td[3]/text()").extract()[0]
    		jobCity=item.xpath("./td[4]/text()").extract()[0]
    		publishTime=item.xpath("./td[5]/text()").extract()[0]

    		print jobName

    		Item["jobName"]=jobName
    		Item["jobLink"]=jobLink
    		Item["jobType"]=jobType
    		Item["recruitNum"]=recruitNum
    		Item["jobCity"]=jobCity
    		Item["publishTime"]=publishTime

    		#将对象传给管道
    		yield Item


    	#处理完一页的内容之后
    	if self.page<2270:
    		self.page+=10
    	

    	#将连接传给调度器，继续爬取，然后回调解析
    	yield scrapy.Request(self.url+str(self.page),callback=self.parse)


    		#ItemList.append(Item)

    	





        
