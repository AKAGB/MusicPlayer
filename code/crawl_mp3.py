"""
测试v1.0
爬取首页排行榜的数据进行测试
"""

import requests
from selenium import webdriver

url = 'http://music.163.com/#/discover/toplist'             # 排行榜页的url

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

