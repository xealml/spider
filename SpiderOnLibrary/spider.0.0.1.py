from selenium import webdriver
import time
driver = webdriver.PhantomJS()
#重新打开网站
driver.get('http://search.ebscohost.com/login.aspx?profile=ehost&defaultdb=pif')
#等待完成跳转
time.sleep(3)
#下拉框中选择
data = driver.find_element_by_xpath('//*[@id="common_PT33"]/option[5]').click()
#点击搜索然后进行跳转
data2 = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_ctrlLimiters_btnSearch"]').click()
#点击进入第一个搜索结果
url = '//*[@id="Result_1"]'
data3 = driver.find_element_by_xpath(url).click()
#此时已经进入了产生搜索结果的界面
#开始进行循环依次进入相应的页面爬取数据
global i
i = 1
while i < 35519:
    print(i)
    #保存成html文件
    makefile = open("./result/"+str(i)+".html","w",encoding='utf-8')
    makefile.write(driver.page_source)
    makefile.close()
    #进入下一个搜索结果
    driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_topNavControl_btnNext"]').click()
    i += 1
