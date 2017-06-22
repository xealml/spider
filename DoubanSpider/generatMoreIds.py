'''
1.使用id拼接url后访问开始
2.抓取每页出现的相关网址
3.存储方式，使用文本方式存放在单行中，中间使用三个#进行分割，左侧为种子id，右侧为
  一个list，使用[]进行包装
'''
from bs4 import BeautifulSoup
import requests
import time

#获取当前页面中的所有的相关联书籍的url
def getText(url):
    web_data = requests.get(url)
    web_data.encoding = 'utf-8'
    html = web_data
    soup = BeautifulSoup(web_data.text,'lxml')
    urls = soup.select('dd > a')
    return html,urls

#将url中的图书ID取出来
def getIds(urls):
    links = []
    moreids = []
    #从网页中获取的所有的标记中得到真实的url
    for url in urls:
        links.append(url.get('href'))
    #从url中取出id
    for id in links:
        moreids.append(id.split('/')[-2])
    return moreids

#当前的编号 相关编号
def wirteTofile(id,moreids):
    
    fw = open('idsInteration.txt','a')
    #fsource = open('test.html','w',encoding= 'utf-8')
    fwids = open('idsIhave.txt','a')

    fw.write(id)
    for _ in moreids:
        fw.write(_)
        if -1 != moreids.index(_):
            fw.write(',')
    fw.write('\n')
    #保存新id
    for _ in moreids:
        fwids.write(_)
        fwids.write('\n')

    #fsource.write(html.text)
    print(moreids)
    fw.close()
    fwids.close()
    #fsource.close()
    #print(getText(url))

freadIds = open('ids.txt','r')
urls = []
i = 1
for _ in freadIds:
    #if i == 3:
        #break
    urls.append('https://book.douban.com/subject/' + str(_))
    i += 1

times = 0
for _ in urls:
    print(_)
    html,urls = getText(_)
    moreids = getIds(urls)
    wirteTofile(_.split('/')[-1],moreids)
    time.sleep(1)
    times += 1
    print(str(times) + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    '''
    if times == 3000:
        time.sleep(100)
    '''




