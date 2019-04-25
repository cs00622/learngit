#coding=utf-8
from lxml import etree
import HtmlDownLoader
import pickle
import downloadjpg
import requests

firurl="https://www.t66y.com/"
m=set() #已经下载的图片
n=set()     #准备下载的图片
paths="e:\\t66yphoto\\"
k=0
j=0
with open('e:/downjpg.plk','rb')as f:   #从文件中读取已下载列表

    m=pickle.load(f)
f.close()



for i in range(1,100):
    firsturl="https://www.t66y.com/thread0806.php?fid=8&search=&page="

    url=firsturl+str(i)

    r = HtmlDownLoader.downloader(url)
    if r==None:
        continue
    html = etree.HTML(r)
    div_mulus = html.xpath('//*[@id="ajaxtable"]/tbody/tr/td/h3/a/@href')
    for div_mulu in div_mulus:
        photourl=firurl+div_mulu

        r = HtmlDownLoader.downloader(photourl)
        html = etree.HTML(r)

        div_photos = html.xpath('.//*[@class="tpc_content do_not_catch"]/input/@data-src')
        for div_photo in div_photos:
            if div_photo in m:

                print("这个图片地址已经存入过集合中")
            else:
                #print(div_photo)
                downloadjpg.downloadjpg(div_photo,paths)

                #print("图片已下载")
                n.add(div_photo)




with open("e:/downjpg.plk","wb")as f:  #将已下载列表写入文件
    pickle.dump(m,f)

f.close()