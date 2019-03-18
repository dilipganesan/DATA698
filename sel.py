#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:08:24 2019

@author: dilipganesan
"""

# Steps for executing this script.

# 1. Do a pip install selenium
# 2. For testing purpose i have set the value of Principal/Secondary Diagnosi
# To Do- Load all the three diagnosis for all the records in pandas DF
# Loop through the values and replace the values in 
# Principal/Secondary diagnosis Codes


from selenium import webdriver
import time

## URL for Find a Code.
url = "https://www.findacode.com/tools/drg-grouper-icd9/"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

#First Time login session.
python_button = driver.find_element_by_link_text('Click here to Sign In')
python_button.click() 
## UserName
element = driver.find_element_by_name("id")
element.send_keys("dilipgan@gmail.com")
## Password
element = driver.find_element_by_name("password")
element.send_keys("data698")
## Sign in 
driver.find_element_by_css_selector(".css_button[value='Sign In']").click()

# Using XPATH to get to the principal diagnosis
element = driver.find_element_by_xpath('//*[@id="sdx_list"]/tr[1]/td[2]/input')
element.send_keys("25083")
# Using XPATH to get to the secondary diagnosis
element = driver.find_element_by_xpath('//*[@id="sdx_list"]/tr[2]/td[2]/input')
element.send_keys("2550")

# Use one more XPATH to get to the secondary diagnosis for 3 diagnosis scenario.
## TODO

# Clicking on the submit button.
driver.find_element_by_id("submit_btn").click()

# Seting a wait time for the frame to refresh.
time.sleep(2)# Based on performance, we can increase wait times.
## Now are switching to iframe.
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
## Selecting the resulting DRG
resultDRG = driver.find_element_by_xpath('/html/body/div/h3')
print("Resultant DRG is -->")
print(resultDRG.text)

## Switch back to main frame
driver.switch_to.default_content()
## Click the Clear Button for next entry.
driver.find_element_by_xpath('//*[@id="btn_clear"]').click()