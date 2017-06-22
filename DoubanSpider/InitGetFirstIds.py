from selenium import webdriver
import threading
import time
import random
from urllib.parse import quote

file = open("./type.data","r",encoding= 'utf-8')
allEles = []
for line in file:
    types = line.split("(")
    types[1] = types[1].split("\t")[1]
    types[2] = types[2].split("\t")[1]
    types[3] = types[3].split("\t")[1]
    for i in range(4):
        allEles.append(types[i])
finished = ['小说','日本','历史']
driver = webdriver.PhantomJS()
for type in allEles:
    '''
    if type == '小说':
        continue
    if type == '日本':
        continue
    if type == '历史':
        continue
    '''
    if type in finished:
        continue
    total = 0
    page = 1
    url = 'https://book.douban.com/tag/'+ type
    urlchange = quote(url, safe='/:?=')
    driver.get(urlchange)
    print("到达指定页面")
    makefile = open("./result/" + type + ".cvs","a",encoding='utf8')
    while 1==1:
        i = 1
        while i < 21:
            try:
                print("开始抓取数据")
                location = driver.find_element_by_xpath('//*[@id="subject_list"]/ul/li['+str(i)+']/div[2]/h2/a')
                title = location.text
                url = location.get_attribute("href")
                score = driver.find_element_by_xpath('//*[@id="subject_list"]/ul/li['+str(i)+']/div[2]/div[2]/span[2]').text
                infomation = driver.find_element_by_xpath('//*[@id="subject_list"]/ul/li['+str(i)+']/div[2]/div[1]').text
                guys = driver.find_element_by_xpath('//*[@id="subject_list"]/ul/li['+str(i)+']/div[2]/div[2]/span[3]').text
                makefile.write(title + "," + url + "," + score + "," + infomation + "," + guys + '\n')
                #print(title + "," + url + "," + score + "," + infomation + "," + guys )
                i += 1
                total += 1
                print(total)
            except:
                print("nope")
                if i == 1:
                    break
                if page  < 11:
                    driver.find_element_by_xpath('//*[@id="subject_list"]/div[2]/span[4]/a').click()
                else:
                    driver.find_element_by_xpath('//*[@id="subject_list"]/div[2]/span[5]/a').click()
                i = 1
                page += 1
                print("page :" + str(page))
            '''
            if total % 120 == 0:
                time.sleep(10)
            '''
        #点击进入下一页
        try:
            if page  < 11:
                driver.find_element_by_xpath('//*[@id="subject_list"]/div[2]/span[4]/a').click()
            else:
                driver.find_element_by_xpath('//*[@id="subject_list"]/div[2]/span[5]/a').click()
            page += 1
            print("page :" + str(page))
        except:
            break
    makefile.close()


