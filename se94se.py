# encoding=utf-8
import sqlite3
import urllib.request
import os
import codecs
import re
class MySql:
	def __init__(self):
		print('建立数据库')
		con=sqlite3.connect("photo.db")
		self.conn=con
		print("获取游标")
		self.cur=con.cursor()
	def create_table(self,sql):
		print("建立表")
		self.cur.execute(sql)
	def execs(self,sql):
		self.cur.execute(sql)
	def get_res(self):
		res=self.cur.execute('select * from photo')
		return res
	def get_save(self):
		self.conn.commit()
class Photo:
	def __init__(self,url):
		#http://94kovv.com/94xx/01/zipaitoupai/20171218251863.html
		data = urllib.request.urlopen(url).read()
		data = data.decode('GBK')
		if "您访问的页面已经更名或迁移" in data:
			print("网站无资源")
			return
		m = re.search("<title>.*</title>", data)
		title=m.group().strip("</title>")
		print(title)
		reg=re.compile('<img src="https:.*?">')
		match = reg.findall(data)
		for colour in match:
			print (colour[10:-2]+"\n")
			try:
				download(colour[10:-2],title)
			except Exception as e:
				print('调用失败')
				return
			
class download:
	def __init__(self,url,title):
		imgPath=r'./photo/'+title
		filesname=url[30:-4]
		#print("下载:",url)
		try:
			UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
			req = urllib.request.Request(url, headers={'User-Agent': UA})
			res=urllib.request.urlopen(req)
			if str(res.status)!='200':
				print('未下载成功：',url)
		except Exception as e:
			print('未下载成功：',url)
		#创建文件夹，用于放图片
		mkdir('photo/'+title)
		filename=os.path.join(imgPath,str(filesname)+'.jpg')
		#print("名字："+filename)
		with open(filename,'wb') as f:
			f.write(res.read())
			print('下载完成\n')
	
def mkdir(path):
    # 引入模块
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
        print (path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        #print (path+' 目录已存在')
        return False
            
if __name__=='__main__':
	#ms=MySql()
	#ms.create_table("create table photo(id integer primary key autoincrement not null,name text,img text)")
	#i=0
	#while True:
	#	i=i+1
	#	ms.execs("insert into photo(name,img) values ('黑小马','135799')")
	#	print(i)
	#	if i==10:
	#		break;
	#res=ms.get_res()
	#for item in res.fetchall():
	#		print(item)
	#ms.get_save()
	mkdir('photo')
	i=20171218251776
	while True:
		url = "http://94kovv.com/94xx/01/zipaitoupai/"+str(i)+".html"
		f = codecs.open('se94se.txt','w','utf-8')
		f.write(url)
		f.close()
		Photo(url)
		i=i-1
		if i==20170401145192:
			break


	
	
	
	
	
	
	
	
