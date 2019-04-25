#coding=utf-8
'''
本程序用于获取自己电脑指定文件夹的所有文件名，并通过相关网站查询到文件所有信息，保存到数据库中

'''
import os
import csv
import downjavinfo
fileinfo=[]             #文件夹中所有文件的列表
rightfilename=[]
filename=[]
urls=[]
fileext=['.mp4','.wmv','.mkv','avi']
path="g:\\film\\"
firsturl="https://www.javbus.pw/"
s = os.sep
root = "g:" + s + "downloads" + s

for i in os.listdir(root):
     if os.path.isfile(os.path.join(root,i)):
#print(fileinfo)
for i in fileinfo:
    '''
    获取文件夹中，符合文件后缀名要求的所有文件
    '''
    fext=os.path.splitext(i)[-1]


    if fext in fileext:
        rightfilename.append(i)
        filename.append(os.path.splitext(i)[0])


for j in filename:
    url=firsturl+j
    urls.append(url)
movieinfo=[]
for m in urls:
    print(m)
    files=downjavinfo.downjavinfo(m)
    if files is None:
        continue
    movieinfo.append(files)

print(movieinfo)
# 将信息写入CSV文件中
f = open('e:\\test.csv', 'a', newline='',encoding='utf-8')
csv_write = csv.writer(f, dialect='excel')
for m_i in movieinfo:
    if not (m_i is None):
        csv_write.writerow(m_i)
f.close()
print("文件写入完成")

'''
# 将信息写入CSV文件中
    f = open('e:\test.csv', 'a', newline='',encoding='utf-8')
    csv_write = csv.writer(f, dialect='excel')
    csv_write.writerow(files)
    
    f.close()
    print("文件写入完成")
'''