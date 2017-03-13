from selenium import webdriver
import time
driver = webdriver.PhantomJS()
#driver.get('http://web.b.ebscohost.com/ehost/resultsadvanced?vid=11&sid=8b0394bb-7b2a-4a95-a24e-7902a3799a3b%40sessionmgr104&bdata=JmRiPXBpZiZicXVlcnk9JmNsaTA9UFQzMyZjbHYwPU1vbm9ncmFwaCZsYW5nPXpoLWNuJnR5cGU9MSZzaXRlPWVob3N0LWxpdmU%3d')
driver.get('http://search.ebscohost.com/login.aspx?profile=ehost&defaultdb=pif')
#等待完成跳转
time.sleep(3)
#下拉框中选择
data = driver.find_element_by_xpath('//*[@id="common_PT33"]/option[5]').click()
#点击搜索然后进行跳转
data2 = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_ctrlLimiters_btnSearch"]').click()
time.sleep(3)
#此时已经进入了产生搜索结果的界面
#开始进行循环依次进入相应的页面爬取数据
global i
i = 1
global times
global nextpages

'''
'每10个结果重新打开依次网站
'''
#---------------------------------------------
fx = file("./result2/result.txt","w")
#---------------------------------------------
for page in xrange(3552):
    print str(page) + "----------------------------------------------"
    times = 1
    while i < 35599:
              
        url = '//*[@id="Result_' + str(i) +'"]'
        data3 = driver.find_element_by_xpath(url).click()
        
        print "处理第" + str(i)+ "结果"
        f = file("./result2/result.txt","a")
        f.write(("Result "+str(i)+"\n").encode("utf-8"))
        title = driver.find_element_by_xpath('//*[@id="citationFields"]/dd[1]/a/span').text
        makefile = file("./result2/"+str(i)+".html","w")
        html = driver.page_source
        #print html
        makefile.write(html.encode("utf-8"))
        makefile.close()
        writer = driver.find_element_by_xpath('//*[@id="citationFields"]/dt[2]').text
        writername = driver.find_element_by_xpath('//*[@id="citationFields"]/dd[2]/a').text
        print "title:" + title
        print writer + writername
        f.write(("title:" + title + "\n").encode("utf-8"))
        f.write((writer + writername + "\n").encode("utf-8"))
        j = 3
        for j in xrange(3,16):
            try:
                left = driver.find_element_by_xpath('//*[@id="citationFields"]/dt['+str(j)+']').text
                right = driver.find_element_by_xpath('//*[@id="citationFields"]/dd['+str(j)+']').text
                rigth = driver.find_element_by_xpath('//*[@id="citationFields"]/dd['+str(j)+']/a').text
            except:
                print ""
            print left + right
            f.write((left + right + "\n").encode("utf-8"))
            j += 1
        f.close()
        #防止被发现
        #time.sleep(3)
        driver.back()
        i += 1
        if times % 10 == 0:
            times += 1
            #重新打开网站
            driver.get('http://search.ebscohost.com/login.aspx?profile=ehost&defaultdb=pif')
            #等待完成跳转
            #time.sleep(3)
            #下拉框中选择
            data = driver.find_element_by_xpath('//*[@id="common_PT33"]/option[5]').click()
            #点击搜索然后进行跳转
            data2 = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_ctrlLimiters_btnSearch"]').click()
            nextpages = i / 10
            while nextpages != 0:
                driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_bottomMultiPage_lnkNext"]').click()
                nextpages -= 1
            break;
        times += 1
    #循环完毕点击下一页
    #driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_bottomMultiPage_lnkNext"]').click()
    print "Next page"
