from selenium import webdriver
import time
driver = webdriver.PhantomJS()
global i
lefttime = 30               #���滹��Ҫ����10��
i = 10307
everytime = 1300
while lefttime != 0:
    
    #��ʼ������ָ��ҳ��
    driver.get('http://search.ebscohost.com/login.aspx?profile=ehost&defaultdb=pif')#���´���վ
    time.sleep(3)#�ȴ������ת
    driver.find_element_by_xpath('//*[@id="common_PT33"]/option[5]').click()#��������ѡ��
    driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_ctrlLimiters_btnSearch"]').click()#�������Ȼ�������ת

    got = everytime#ÿ����ȥ2000��
    #��ת����pageҳ
    page = i / 10
    nextpages = page
    
    while nextpages != 0:
        print nextpages
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContentArea_MainContentArea_bottomMultiPage_lnkNext"]').click()
        nextpages -= 1
    url = '//*[@id="Result_' + str(i) +'"]'
    driver.find_element_by_xpath(url).click()
    #��ʼ��ȥ����
    while i < 35519:
        print(i)
        
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

        
