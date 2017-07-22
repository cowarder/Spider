#coding=utf-8
#qiushi.py

#模糊查询
#根节点
#//div[contains(@id,"qiushi_tag_")]

#用户名
#./div/a/title[0]

#段子的内容
#.//div/[@class="content"]/span

#点赞
#.//i[0]

#评论
#.//i[1]

#图片的链接
#.//[@class,"thumb"]@src

#url
#https://www.qiushibaike.com/imgrank/page/1/

import json
import urllib
from  lxml import etree
import urllib
import urllib.request

url="https://www.qiushibaike.com/imgrank/page/2/"
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
 }
request=urllib.request.Request(url,headers=headers)
response=urllib.request.urlopen(request).read()
#利用获取html文件
html=response.decode("utf8")
#将html文件解析为HTML DOM格式文件
text=etree.HTML(html)
print(text)
#返回每一条段子的结点，contains是进行模糊匹配
node_list=text.xpath('//div[contains(@id,"qiushi_tag")]')
items={}
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

with open("qiushi.json","a") as f:
	#解析为json格式字符串
	f.write(json.dumps(items,ensure_ascii=False)+"\n")







