#condig=utf-8
import urllib.request
import urllib

from PIL import Image

def downloadjpg(jpgurl,path):
    '''
    下载图片，图片网址为jpgurl,下载到磁盘的path文件夹中

    :param jpgurl:
    :param path:
    :return:
    '''
    filename=jpgurl.split('/')[-1]
    #print(filename)

    fullpath=path+filename
    print(fullpath)
    print(jpgurl)
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(jpgurl,fullpath)
        print("图片下载成功")


        img=Image.open(fullpath)    #获取已下载图片的尺寸
        (x,y)=img.size
        print("图片的尺寸为%d,%d"%(x,y))
    except:
        print("图片下载失败")