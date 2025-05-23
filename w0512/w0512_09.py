import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import time
# 크롬 옵션 설정
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# 브라우저 실행
browser = webdriver.Chrome(options=options)
# 쿠팡 페이지 접속
url = "https://www.gmarket.co.kr/n/best"
browser.get(url)
time.sleep(3)#페이지 로딩대기
print(browser.page_source)
soup=BeautifulSoup(browser.page_source,"lxml")


data = soup.find("ul",{"class":"list__best"})
data2 = data.find_all("li",{"class":"list-item"})
fish = data2[0].find("a").get_text()
print(fish)