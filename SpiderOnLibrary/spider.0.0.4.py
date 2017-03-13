from selenium import webdriver
import time
driver = webdriver.PhantomJS()
#重新打开网站
driver.get('http://search.ebscohost.com/login.aspx?profile=ehost&defaultdb=pif')
#等待完成跳转
time.sleep(3)
#下拉框中选择
driver.find_element_by_xpath('//*[@id="common_PT33"]/option[5]').click()
#点击搜索然后进行跳转
driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_ctrlLimiters_btnSearch"]').click()
global i
i = 6001
#跳转到第page页
page = 601
nextpages = page - 1
while nextpages != 0:
    #print nextpages
    print(nextpages)
    driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_bottomMultiPage_lnkNext"]').click()
    nextpages -= 1

#点击进入第2501个搜索结果
url = '//*[@id="Result_' + str(i) +'"]'
driver.find_element_by_xpath(url).click()
while i < 35519:
    print(i)
    #保存成html文件
    makefile = open("./result6000/"+str(i)+".html","w",encoding='utf-8')
    #makefile = file("./result6000/"+str(i)+".html","w")
    #makefile.write(driver.page_source.encode("utf-8"))
    makefile.write(driver.page_source)
    makefile.close()
    #进入下一个搜索结果
    driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_topNavControl_btnNext"]').click()
    i += 1
