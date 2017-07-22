#coding=utf-8
import urllib2;

url_headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

}
#构造一个请求对象
request=urllib2.Request("http://www.baidu.com/",headers=url_headers);

#向指定的URL地址发送请求，返回服务器返回的类文件对象
response=urllib2.urlopen(request);

#read读取全部内容
html=response.read();

#返回响应码，200成功
#print response.getcode();

#print response.geturl();


print html;
