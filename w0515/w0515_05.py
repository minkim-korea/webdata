### 네이버 항공권 
# 김포 , 제주 5/31 6/1  
# 금액 1100000원 이상은 제외 
# 김포출발시간 17:00 이후는 제외 


import pyautogui  # 마우스 제어

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import time
import random

# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 창 최대화

### 1. 네이버 항공권 접속
url = "https://flight.naver.com/"
browser.get(url)

time.sleep(2)

### 2. 팝업창 닫기
elem = browser.find_element(By.CLASS_NAME,'FullscreenPopup_close')
elem.click()
time.sleep(2)

# 3. 출발지 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]/b')
elem.click()
time.sleep(2)

# # 4. 김포선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div/div/ul[1]/li[3]/button')
elem.click()
time.sleep(2)

# # 5. 도착지 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]/b')
elem.click()
time.sleep(2)

# # 6. 제주선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[2]/div[2]/ul[1]/li[1]/button').click()
time.sleep(2)

# # 7. 가는날 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2) 

# 8. 출발날짜 선택   
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[5]/td[7]/button/b').click()
time.sleep(2)
# 9. 도착날짜 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/button/b').click()
time.sleep(2)

# 10. 항공권 검색 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button').click()

# # 11. 항공권 출력할때까지 대기
# # 검색버튼 클릭후 화면이 나타날때까지 대기하고 길게는 10초 대기
# # WebDriverWait(browser,10).until(EC.presence_of_all_elements_located(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]/div[2]/div[1]'))
time.sleep(7)

### 스크롤 내리기
# 현재 사이트 높이를 가져오는 자바스크립트
prev_height = browser.execute_script("return document.body.scrollHeight")

# 
standard_time= datetime.strptime("17:00", "%H:%M").time()
# 반복 실행
while True:
    # 현재 브라우저에서 0에서 현재 높이까지 스크롤 내리기
    # 자바스크립트 실행
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    # 변동된 현재 문서 높이을 가져오기
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 스크롤 높이가 변동이 없을시
    if curr_height == prev_height: break 
    prev_height = curr_height # 현재 높이를 다시 입력해서 스크롤 내리기 재실행

print("스크롤 내리기 종료")

soup = BeautifulSoup(browser.page_source,"lxml")
datas = soup.find_all("div",{"class":"domestic_Flight__8bR_b"})
for data in datas :
# 금액 
    price = data.find("i",{"class":"domestic_num__ShOub"})
    prices = int(price.get_text().replace(",",""))
      #출발시간 
    departs = data.find("span",{"class":"route_airport__tBD9o"})
    departs = departs.get_text()
    depart_line = departs.split("G")
    depart_time = datetime.strptime(depart_line[0], "%H:%M").time()
    datas = data.find("b",{"class":"airline_name__0Tw5w"})
    datas = datas.get_text()
    if prices <= 110000 and depart_time<standard_time :
       print(datas)
       print(prices)
       print(depart_time)

    
    
    
 
      







### 프로그램종료
input("프로그램 종료(엔터키)")
