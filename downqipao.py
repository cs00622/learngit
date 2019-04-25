#coding=utf-8
'''下载太平洋电脑网摄影论坛的照片'''
import requests
from lxml import etree
import pickle
import downloadjpg
import  HtmlDownLoader




url="https://itbbs.pconline.com.cn/dc/f2312647_1.html"

r=HtmlDownLoader.downloader(url)

html=etree.HTML(r)
div_mulus=html.xpath('.//*[@class="tit toe"]/@href')
div_mulu=""
i=0
j=0
k=0
m=set()      #文件中读取的已下载图片集合

l=set()     #需要下载的图片集合
with open('e:/download.plk','rb')as f:   #从文件中读取已下载列表

    m=pickle.load(f)
f.close()

for div_mulu in div_mulus:
    i=i+1
    html1="http:"+div_mulu
    #print(html1)
    s=HtmlDownLoader.downloader(html1)
    print("已经分析了%d个页面"%i)
    html2=etree.HTML(s)
    div_photos=html2.xpath('.//div[@class="topiccontent"]/span/img/@src2')
    for div_photo in div_photos:
        jpgurl="http:"+div_photo
        if (jpgurl in m):   #判断图片地址是否存在于已分析完的地址中
            print("这个图片地址已经存入过集合中")
        else:
            l.add(jpgurl)   #如果未下载过，就把图片地址写入集合
        #print(jpgurl)
print("总共有%d张图片存在于集合中,还需要下载%d张图片。"%(len(m),len(l)))
path="g:\downjpg\\"

try:
    for z in l:
        downloadjpg.downloadjpg(z,path)
        m.add(z)
        k=k+1
        print("这是下载完成的第%d张图片"%k)
except:
    print("图片下载失败，继续下一个")
    j=j+1
print('共计下载图片%d张，另有%d个图片下载失败'%(k,j))

with open("e:/download.plk","wb")as f:  #将已下载列表写入文件
    pickle.dump(m,f)

f.close()
print("文件下载完成，数据库中有%d张图片，本次下载了%d张图片"%(len(m),len(l)))
#print(l)