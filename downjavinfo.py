#coding=utf-8
import  HtmlDownLoader
from lxml import etree
def downjavinfo(url):
    r=HtmlDownLoader.downloader(url)
    if r is None:
        print("没有找到相关信息")
        return None
    html=etree.HTML(r)
    div_mulus = html.xpath('.//*[@class="container"]/div/div/a/img/@title')  # 获取电影名称
    div_mulu = ""
    for div_mulu in div_mulus:
        print(div_mulu)

    div_names = html.xpath('.//*[@class="container"]/div/div/p/span[@style="color:#CC0000;"]/text()')  # 获取电影识别码
    div_name = ""
    for div_name in div_names:
        pass
        #print(div_name)

    div_datas = html.xpath('.//*[@class="container"]/div/div/p[span="發行日期:"]/text()')  # 获取发行日期
    div_data = ""
    for div_data in div_datas:
        print(div_data)

    div_lens = html.xpath('.//*[@class="container"]/div/div/p[span="長度:"]/text()')  # 获取长度
    div_len = ""
    for div_len in div_lens:
        print(div_len)

    div_zizuosans = html.xpath('.//*[@class="container"]/div/div/p[span="製作商:"]/a/text()')  # 获取制作商
    div_zizuosan = ""
    for div_zizuosan in div_zizuosans:
        print(div_zizuosan)

    div_faxinsans = html.xpath('.//*[@class="container"]/div/div/p[span="發行商:"]/a/text()')  # 获取发行商
    div_faxinsan = ""
    for div_faxinsan in div_faxinsans:
        print(div_faxinsan)

    div_xilies = html.xpath('.//*[@class="container"]/div/div/p[span="系列:"]/a/text()')  # 获取系列
    div_xilie = ""
    for div_xilie in div_xilies:
        print(div_xilie)

    div_lvyous = html.xpath(
        './/*[@class="container"]/div/div[@class="col-md-3 info"]/p/span[contains(@onmouseover,"hoverdiv")]/a/text()')  # 获取演员
    div_lvyou_s = ""
    for div_lvyou in div_lvyous:
        div_lvyou_s = div_lvyou_s + div_lvyou + " "
    print(div_lvyou_s)

    div_types = html.xpath(
        './/*[@class="container"]/div/div[@class="col-md-3 info"]/p/span[@class="genre"]/a/text()')  # 获取类型
    div_type_s = ""
    for div_type in div_types:
        div_type_s = div_type_s + div_type + " "
    #print(div_type_s)
    div_type_s=div_type_s.replace('\(','')
    div_type_s=div_type_s.replace('\)','')
    div_type_s = div_type_s.strip(div_lvyou_s)
    print(div_type_s)
    header = ['编号', '电影名称', '发行日期', '电影片长', '制作商', '发行商', '系列', '电影类型', '女优']
    content = [div_name, div_mulu, div_data, div_len, div_zizuosan, div_faxinsan, div_xilie, div_type_s, div_lvyou_s]
    return content