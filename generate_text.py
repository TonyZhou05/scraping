from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import re

driver = webdriver.Chrome((ChromeDriverManager().install()))
websiteList = set()

def get_body(driver):
    element = driver.find_element(By.XPATH, "/html/body")
    time.sleep(5)
    # content = re.sub('\n', ' ', element.text)
    # string = content.encode("utf-8")
    # print(element.text)
    content = element.text
    content = re.sub('\n', ' ', content)
    return content

readf = open('website_lists/version1.txt', 'r')
Lines = readf.readlines()


for line in Lines:
    if line in websiteList: continue
    websiteList.add(line)
    companyName = line.split('.')[1]
    driver.get(line)
    # create json data instance
    data = {}
    data['body'] = get_body(driver)
    file = open('./contents/' + companyName + '.txt', 'a')
    file.write(data['body'])
    file.close()
