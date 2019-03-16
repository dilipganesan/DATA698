# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 22:07:19 2019

@author: Admin
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
import time
import pandas as pd 

# import data into python envirenment
data = pd.read_csv("C:/Users/Admin/Dropbox/data698/DRG_0_to_250.csv") 
#data["DRG"]=""
#data["Payment"]=""
data=data.fillna("")

#data.reset_index(drop=True, inplace=True)
#print(data.index.name)
#list(data)
#data.drop(data.columns[[0,1]], axis=1, inplace=True)

#data.to_csv("DRG_1499_to_1749.csv", index=False)


NewFileName=""

## URL for Find a Code.
url = "https://www.findacode.com/tools/drg-grouper-icd9/"

# create a new Firefox session
driver = webdriver.Chrome("C:\\Users\\Admin\\Desktop\\Data698\\chromedriver_win32\\chromedriver")
#driver.implicitly_wait(50)
driver.get(url)

#First Time login session.
python_button = driver.find_element_by_link_text('Click here to Sign In')
python_button.click() 
## UserName
element = driver.find_element_by_name("id")
element.send_keys("dilipgan@gmail.com")
# Password
element = driver.find_element_by_name("password")
element.send_keys("data698")
time.sleep(5)
# Sign in 
driver.find_element_by_css_selector(".css_button[value='Sign In']").click()

# max: 101766
# 498
inc=251
for j in range(0,3):
    Min=inc
    Max=inc+250
    if Max > 916:
        Max=916
    s1="DRG_" + str(Min)
    s2="_to_"+ str(Max)
    s3=".csv"
    NewFileName=s1+s2+s3
    
    print(NewFileName)
    
    for i in range(Min, Max):
        
    # Using XPATH to get to the principal diagnosis
        if(data.iloc[i][0] != "" and  pd.isnull(data.iloc[i][0]) == False):
             try:
                 element = driver.find_element_by_xpath('//*[@id="sdx_list"]/tr[1]/td[2]/input')
                 element.send_keys(data.iloc[i][0])   
                 time.sleep(.25)
                 driver.find_element_by_id("submit_btn").click()
             except NoSuchElementException as exception:
                 print("Element not found and test failed setting INPUT")
                
    
    # Seting a wait time for the frame to refresh.
        time.sleep(1)# Based on performance, we can increase wait times.
    ## Now are switching to iframe.
        
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    ## Selecting the resulting DRG
        try:
            resultDRG = driver.find_element_by_xpath('/html/body/div/h3')
            rDRG =  [int(s) for s in resultDRG.text.split() if s.isdigit()][0]
            rDRG=str(rDRG)
            data.iloc[i][1]=str(rDRG)
        except NoSuchElementException as exception:
            print("Element not found and test failed getting DRG ")
    # switch back to element content 
        driver.switch_to_default_content
    
    # get the payments
        try:
            paymentDRG = driver.find_element_by_xpath('//*[@id="sh_pay_calc_div"]/div[2]/table/tbody/tr[2]/td[3]')
            if(paymentDRG != ""):
                pDRG=re.sub('[\$,]','', paymentDRG.text)
                print(i," DRG: ",rDRG," PDRG:",pDRG)
                data.iloc[i][2]=pDRG
        except NoSuchElementException as exception:
            print("Element not found and test failed getting PAYMENT")
    
    ## Switch back to main frame
        driver.switch_to.default_content()
    ## Click the Clear Button for next entry.
        driver.find_element_by_xpath('//*[@id="btn_clear"]').click()
        time.sleep(1.75)
    data.to_csv(NewFileName, index=False)
    time.sleep(1) 
    
    inc = i+1

driver.close()