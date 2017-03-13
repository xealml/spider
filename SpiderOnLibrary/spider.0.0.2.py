from selenium import webdriver
import time
driver = webdriver.PhantomJS()
global i
lefttime = 30               #爬虫还需要启动10次
i = 10307
everytime = 1300
while lefttime != 0:
    
    #初始化到达指定页面
    driver.get('http://search.ebscohost.com/login.aspx?profile=ehost&defaultdb=pif')#重新打开网站
    time.sleep(3)#等待完成跳转
    driver.find_element_by_xpath('//*[@id="common_PT33"]/option[5]').click()#下拉框中选择
    driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_ctrlLimiters_btnSearch"]').click()#点击搜索然后进行跳转

    got = everytime#每次爬去2000个
    #跳转到第page页
    page = i / 10
    nextpages = page
    
    while nextpages != 0:
        print nextpages
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_bottomMultiPage_lnkNext"]').click()
        nextpages -= 1
    url = '//*[@id="Result_' + str(i) +'"]'
    driver.find_element_by_xpath(url).click()
    #开始爬去数据
    while i < 35519:
        print(i)
        
        #保存成html文件
        makefile = file("./result/"+str(i)+".html","w")
        makefile.write(driver.page_source.encode("utf-8"))
        makefile.close()

        got -= 1
        i += 1
        if got == 0:
            break;

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_topNavControl_btnNext"]').click()#进入下一个搜索结果
    lefttime -=1

        
