#coding=utf-8
import requests
from fake_useragent import UserAgent  #获取随机的UA信息


def downloader(url):
    if url is None:
        return None
    ua = UserAgent()  # 随机获取文件头
    headers = {'User-Agent': ua.random}
    try:
        r=requests.get(url,headers=headers,timeout=15)
        if r.status_code==200:
            return r.text
    except:
        return None

