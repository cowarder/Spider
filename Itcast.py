#-*- coding: UTF-8 -*- 
import scrapy
from ItCast.items import ItcastItem
class ItCastSpider(scrapy.Spider):
	#爬虫的名字
	name="itcast"
	#爬虫作用的范围
	allowd_domain=["http://http://www.itcast.cn/"]
	#爬虫的url
	start_urls=["http://www.itcast.cn/channel/teacher.shtml#"]

	def parse(self,response):
		#with open("D:/teacher.html","w") as f:
		#	f.write(response.body)
		#通过Scrapy自带的xpath匹配出所有老师
		teacher_list=response.xpath('//div[@class="li_txt"]')

		teacherItem=[]
		#遍历列表集合
		#xpath返回的都是列表
		for item in teacher_list:
			Item=ItcastItem()
			#如果取的是标签里面的内容，需要加text
			#name
			name=item.xpath("./h3/text()").extract()
			#title
			title=item.xpath("./h4/text()").extract()
			#info
			info=item.xpath("./p/text()").extract()

			Item["name"]=name[0].encode("gbk")
			Item["title"]=title[0].encode("gbk")
			Item["info"]=info[0].encode("gbk")

			teacherItem.append(Item)
			print name
			print title
			print info
		return teacherItem