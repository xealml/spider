from selenium import webdriver
import time
driver = webdriver.PhantomJS()
global i
lefttime = 12               #���滹��Ҫ����10��
i = 35115
everytime = 2000
amountInEverypage = 50
while lefttime != 0:

    #��ʼ������ָ��ҳ��
    driver.get('http://search.ebscohost.com/login.aspx?profile=ehost&defaultdb=pif')#���´���վ
    time.sleep(3)#�ȴ������ת
    driver.find_element_by_xpath('//*[@id="common_PT33"]/option[5]').click()#��������ѡ��
    driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_ctrlLimiters_btnSearch"]').click()#�������Ȼ�������ת
    driver.find_element_by_xpath('//*[@id="lnkPageOptions"]').click()#ҳ��ѡ��
    driver.find_element_by_xpath('//*[@id="pageOptions"]/li[3]/ul/li[6]/a').click()#��ҳ��ʾ50��
    

    got = everytime
    #��ת����pageҳ
    page = i / amountInEverypage
    if i % amountInEverypage == 0:
        page -= 1
    nextpages = page
    
    #1����ǿ����ָ��ҳ�������
    while nextpages != 0:
        print nextpages
        if nextpages > 5:
            driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_bottomMultiPage_rptPageLinks_ctl04_lnkPageLink"]').click()
            driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_bottomMultiPage_lnkNext"]').click()
            nextpages -= 5
        else:
            driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_bottomMultiPage_lnkNext"]').click()
            nextpages -= 1
    url = '//*[@id="Result_' + str(i) +'"]'
    driver.find_element_by_xpath(url).click()
    result_i = 0
    #��ʼ��ȥ����
    while i < 35519:
        result_i += 1
        print(str(i) +"\t"+ str(result_i))
        
        #�����html�ļ�
        makefile = file("./result/"+str(i)+".html","w")
        makefile.write(driver.page_source.encode("utf-8"))
        makefile.close()

        got -= 1
        i += 1
        if got == 0:
            break;

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_topNavControl_btnNext"]').click()#������һ���������
    lefttime -=1

        
