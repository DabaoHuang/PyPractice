# pip install requests
"""import requests

res = requests.get("http://pala.tw/js-example/")
print(res.text)"""


from selenium import webdriver
import sys

#python d:/GIT/PyPractice/hello.py http://pala.tw/js-example/

driver = webdriver.PhantomJS(executable_path="D:\GIT\PyPractice\phantomjs-2.1.1\jin\phantomjs")

try:
    url = sys.argv[1]
except IndexError:
    url = 'null'

if url == 'null':
    print("Error: not get url")
else:
    driver.get(url)    
    pageSource = driver.page_source
    print(pageSource)

driver.close()