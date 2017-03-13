from selenium import webdriver
import time
driver = webdriver.PhantomJS()
global i
lefttime = 12               #剩余启动次数
i = 35115                   #开始编号，如果被服务器发现爬数据报错误，直接从正确爬去编号的下一个爬取
everytime = 2000            #每次抓取的数据的个数，测试发现1000最合适
amountInEverypage = 50      #单页显示数量，配合每页显示的个数可以大幅度减少导航时间
while lefttime != 0:

    #初始化到达指定页面
    driver.get('http://search.ebscohost.com/login.aspx?profile=ehost&defaultdb=pif')#重新打开网站
    time.sleep(3)                                                                   #等待完成跳转
    driver.find_element_by_xpath('//*[@id="common_PT33"]/option[5]').click()        #下拉框中选择
    driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_ctrlLimiters_btnSearch"]').click()#点击搜索然后进行跳转
    driver.find_element_by_xpath('//*[@id="lnkPageOptions"]').click()               #页面选项
    driver.find_element_by_xpath('//*[@id="pageOptions"]/li[3]/ul/li[6]/a').click() #单页显示50个
    

    got = everytime         #单次爬去数据量倒计时
    #跳转到第page页
    page = i / amountInEverypage
    if i % amountInEverypage == 0:
        page -= 1
    nextpages = page        #需要跳转的次数
    
    #1）增强到达指定页面的能力
    while nextpages != 0:
        print nextpages
        if nextpages > 5:
            #大跳步
            driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_bottomMultiPage_rptPageLinks_ctl04_lnkPageLink"]').click()
            #小跳步
            driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_bottomMultiPage_lnkNext"]').click()
            nextpages -= 5
        else:
            driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_bottomMultiPage_lnkNext"]').click()
            nextpages -= 1
    url = '//*[@id="Result_' + str(i) +'"]'     #获取进入页面的url
    driver.find_element_by_xpath(url).click()   #点击进入
    result_i = 0                                #辅助显示爬去序号
    #开始爬去数据
    while i < 35519:
        result_i += 1
        print(str(i) +"\t"+ str(result_i))
        
        #保存成html文件
        makefile = file("./result/"+str(i)+".html","w")
        makefile.write(driver.page_source.encode("utf-8"))
        makefile.close()

        got -= 1
        i += 1
        if got == 0:
            break;
        #下一项
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_topNavControl_btnNext"]').click()#进入下一个搜索结果
    lefttime -=1

        
