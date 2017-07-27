# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class ItcastPipeline(object):
	#init可选，初始化方法
	def __init__(self):
		#创建一个文件
		self.filename=open("teacher.json","w")

	def process_item(self, item, spider):
		jsontext=json.dumps(dict(item),ensure_ascii=False)+"\n"
		self.filename.write(jsontext)
		return item  

    #结束时调用，可选
	def close_spider(self):
		self.filename.close()
