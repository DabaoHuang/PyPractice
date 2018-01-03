#coding=utf-8

from selenium import webdriver
import time
import json

driver = webdriver.Firefox()
driver.get("https://www.victoriassecret.com/bras/select-bras-special-sale/push-up-bra-dream-angels?ProductID=360639&CatalogueType=OLS")

time.sleep(10)
driver.find_element_by_name("HEADER: GEFOC").click()
time.sleep(5)
driver.find_element_by_id("north-america").click()
time.sleep(1)
driver.find_element_by_xpath('//a[@data-country="US"]').click()
driver.find_element_by_id('save').click()

cookie= driver.get_cookies()

#将获得cookie的信息打印
print(cookie)
encodedjson =  json.dumps(cookie)

text_file = open("Output.txt", "w")
text_file.write("Purchase Amount: %s" % encodedjson)
text_file.close()

driver.quit()