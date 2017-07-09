import urllib2
import re

class Spider:
	def __init__(self):
		"""
			page:初始化下载的起始页
			switch:下载开关
		"""
		self.page=2
		self.switch=True

	def loadPage(self):
		"""
			加载HTML文本文件
		"""
		url="http://www.neihan8.com/article/index_"+str(self.page)+".html"

		headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
		#构建一个request对象
		request=urllib2.Request(url,headers=headers)
		#接受返回的类文本对象
		response=urllib2.urlopen(request)
		#拿到HTML文本文件
		html=response.read()
		#构建正则表达式
		pattern=re.compile('<div\sclass="desc">(.*?)</div>',re.S)
		#正则表达式应用
		content_list=pattern.findall(html)
		#下载爬取文本到本地文件夹
		self.savaPage(content_list)

	def savaPage(self,content_list):
		"""
			下载爬取文本到本地文件夹
		"""

		for item in content_list:
			with open("duanzi.txt","a") as f:
				f.write(item)
				f.write("\r\n")
				f.write("\r\n")
		print "第"+str(self.page)+"下载完毕！"

	def duanziSpider(self):
		while self.switch:
			switch=raw_input("继续加载下一页请按回车，退出输入exit:")
			if(switch=="exit"):
				self.switch=False
			else:
				self.loadPage()
				self.page+=1


if __name__=="__main__":
	duanziSpider=Spider()
	duanziSpider.duanziSpider()
	print "谢谢使用！"



