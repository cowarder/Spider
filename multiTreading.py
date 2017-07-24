#coding=utf-8

import threading
import json
import requests
from lxml import etree
import queue

CRAW_EXIT=False
PARSE_EXIT=False

class crawlThread(threading.Thread):
	"""
		threadName:线程名
		pageQueue:页码队列
		dataQueue:获取到的html文本队列
		构建爬虫线程类，获取每个页面的html
	"""
	def __init__(self,threadName,pageQueue,dataQueue)
		#对父类进行初始化
		super(crawlThread,self).__init__()
		self.threadName=threadName
		self.pageQueue=pageQueue
		self.dataQueue=dataQueue

	def run(self):
		print("线程"+self.threadName+"开始")
		while not CRAW_EXIT:
			try:
				# 取出一个数字，先进先出
                # 可选参数block，默认值为True
                #1. 如果对列为空，block为True的话，不会结束，会进入阻塞状态，直到队列有新的数据
                #2. 如果队列为空，block为False的话，就弹出一个Queue.empty()异常，
				page=self.pageQueue.get(False)
				headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36" }
				url="https://www.qiushibaike.com/imgrank/page/"+str(page)+"/"
				//获取html字符串
				response=requests.get(url,headers=headers).text
				time.sleep(1)
				self.dataQueue.put(response)
			except:
				pass
		print("线程"+self.threadName+"结束")

class parseThread(threading.Tread):
	"""
		threadName:线程名字
		dataQueue:由爬虫多线程任务获取到的html字符串
		fileName:解析后的文件存储位置
		lock:锁
		对html(dataQueue)文件进行解析，提取需要的信息
	"""
	def __init__(self,threadName,dataQueue,fileName,lock):
		#对父类进行初始化
		super(parseThread,self).__init__()
		self.threadName=threadName
		self.dataQueue=dataQueue
		self.fileName=fileName
		self.lock=lock
	
	def run(self):
		print("解析线程"+self.threadName+"开始")
		while not PARSE_EXIT:
			try:
				data=self.dataQueue.get(False)
				self.parse(data)
			except:
				pass
		print("解析线程"+self.threadName+"结束")

	def parse(self,data):
		//解析为HTML DOM文件
		text=etree.HTML(data)
		items={}
		node_list=text.xpath('//div[contains(@id,"qiushi_tag")]')
		for node in node_list:
			#带有@的是直接取其中的值
			username=node.xpath(".//div/a/@title")[0]
			#取出标签下的内容
			content=node.xpath(".//div[@class='content']/span")[0].text
			"""
				xpath返回的是一个列表，如果不加下标就会是列表，加了返回字符串
			"""
			#图片的地址
			image=node.xpath(".//div[@class='thumb']//@src")
			#赞的个数
			vote=node.xpath(".//i")[0].text
			#评论的个数
			comment=node.xpath(".//i")[1].text

			items={
				"username":username,
				"image":image,
				"content":content,
				"vote":vote,
				"comment":comment
			}

			#不管里面的操作结果是怎样的
			#都会经过打开关闭，打开锁处理内容，释放锁
			with self.lock:
				self.fileName.write(json.dumps(items,ensure_ascii=False)+"\n")


def main():
	#这里声明这两个变量是全局变量
	global CRAW_EXIT
	global PARSE_EXIT

	#用于存放页面队列，表示爬取10个页面：1-10
	pageQueue=queue.Queue(10)
	for i in range(1，11):
		pageQueue.put(i)

	#存放文件名
	fileName=open("multiThread.json","a")

	#创建锁
	lock=threading.lock()

	#用于存放html字符串
	dataQueue=queue.Queue()

	#采集线程名字
	crawlNames=["采集线程1"，"采集线程2","采集线程3"]
	
	#解析线程名字
	parseNames=["解析线程1","解析线程2","解析线程3"]
	
	#存放采集线程
	crawlThreads=[]
	
	#开启采集线程
	for crawlName in crawlNames:
		thread=crawlThread(crawlName,pageQueue,dataQueue)
		thread.start()
		crawlThreads.append(thread)

	#存放解析线程
	parseThreads=[]

	#开启解析线程
	for parseName in parseNames:
		thread=parseThread(parseName,dataQueue,fileName,lock)
		thread.start()
		parseThreads.append(thead)

	#等待页面队列全部取完
	while not pageQueue.empty():
		pass

	print("pageQueu为空")
	CRAW_EXIT=true

	# join() 方法主要是让调用该方法的thread完成run方法里面的东西后， 再执行join()方法后面的代码。
	for thread in crawlThreads:
		thread.join()
		print("1")

	#等待数据全部解析完成
	while not dataQueue.empty():
		pass

	PARSE_EXIT=true
	for thread in parseThreads:
		thread.join()
		print("2")

	with lock:
		#关闭文件
		fileName.close

	print("谢谢使用")

if __name__=="__main__":
	main()









			













