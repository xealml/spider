from bs4 import BeautifulSoup
import requests
import time
import re
import sqlite3

#中英文对照
trans = {
'标题':'title',
'作者':'author',
'丛书':'series',
'出版物信息':'PublicationInformation',
'文献类型':'DocumentType',
'主题':'topic',
'Persons as Subjects':'PersonsasSubjects',
'摘要':'digest',
'ISBN':'ISBN',
'语言':'language',
'Print Edition':'PrintEdition',
'入藏编号':'inputId',
'ISSN':'ISSN'
}
tmpElement = {
'标题':'null',
'作者':'null',
'丛书':'null',
'出版物信息':'null',
'文献类型':'null',
'主题':'null',
'Persons as Subjects':'null',
'摘要':'null',
'ISBN':'null',
'语言':'null',
'Print Edition':'null',
'入藏编号':'null',
'ISSN':'null'
}
'''
获取列名和对应的值的两个列表，这两个列表是一一对应的但是由于有些
网页中的信息不全，导致需要将信息填充进设计好的规则中，没有信息的
部分网页直接填充null进去
'''
def getText(url):
    web_data = open(url,'r',encoding = 'utf-8')
    soup = BeautifulSoup(web_data.read(),'lxml')
    dt = soup.select('dt')      #label
    dd = soup.select('dd')      #value
    return dt,dd

conn = sqlite3.connect('result.db')
i = 10307
j = i + 25213
tmp2list = []
while 1 == 1:
    print(str(j) + ":finished")
    #编号标记，在数据库中唯一
    id = []
    id.append(j)
    #由于网页直接存成 数字.html 的格式，直接迭代
    dt,dd = getText(str(i) + '.html')
    dts = []
    dds = []
    #key:去掉其中的回车
    for _ in dt:
        _.text.replace('\n','')
        dts.append(_.text[:-1])
    #value：去除回车和部分html转义，这个应该没有将全部信息覆盖到，不过看到解析完的数据还可以
    for _ in dd:
        tmpsoup = BeautifulSoup(str(_),'lxml')
        if tmpsoup.string == None:
            strresult = ''
            tmp = tmpsoup.findAll('a')
            for element in tmp:
                strresult += element.text + '---'
            dds.append(strresult)
        else:
            regex = re.compile(r'(\n|\xa0)')
            ddtext = re.subn(regex,'',_.text)
            dds.append(ddtext[0])
    #合并成字典
    result = dict(zip(dts,dds))
    tmp2 = tmpElement.copy()
    #填充:_迭代的是字典中的键，使用值填充
    for _ in result:
        tmp2[_] = result[_]
    for _ in tmp2.values():
        tmp2list.append(_)
    #部分网页中的信息也是13条，但是由于在抓取网页存储的时候产生了乱码
    #这个时候再去使用字典进行匹配匹配不到，数据表中添加一个extra进行兼容
    #性加强，再产生诸如摘要由于存储变成摘#的时候生成最后一列的信息
    if len(tmp2list) == 13:
        tmp2list.append('null')
    conn.execute('INSERT INTO information values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',id + tmp2list)
    conn.commit()
    i += 1
    j += 1
print('finished!')
conn.close()
