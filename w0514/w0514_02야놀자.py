import requests
from bs4 import BeautifulSoup
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
url = "https://nol.yanolja.com/"
browser.get(url)
## 화면닫기
time.sleep(2)
browser.find_element(By.XPATH,'/html/body/div[10]/div/div/div/section/div[2]/button[2]').click()
## 호텔/리조트 클릭
time.sleep(1)
browser.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/a[11]/div').click()
## 지역선택
browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div/div/button').click()
## 제주 선택
time.sleep(1)
browser.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div/div/div[1]/button[3]').click()
## 서귀포시/모슬포 선택
browser.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div/div/div[2]/div[1]/a[2]').click()
## 날짜 선택
time.sleep(1)
browser.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/header/div[2]/div/button[1]').click()
## 가는날짜 선택
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="day-picker-2025-06"]/div[2]/div[1]/div[7]/button').click()
## 오는날짜 선택
browser.find_element(By.XPATH,'//*[@id="day-picker-2025-06"]/div[2]/div[2]/div[1]/button').click()
## 적용버튼 선택
browser.find_element(By.XPATH,'//*[@id="pc-dialog-sheet"]/div/div/div[3]/button').click()
## 스크롤 내리기
time.sleep(1)
# 현재높이 가져오기 - 1000
prev_height = browser.execute_script("return document.body.scrollHeight")
while True: #무한반복 - 높이가 더이상 늘어나지 않을때까지
    # 스크롤내리기 - 0에서 현재높이까지 스크롤이 내려감.
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    # 변경된 현재높이 가져오기
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 높이가 변경되었는지 확인
    if prev_height == curr_height:
        break
    # 현재높이를 이전높이변수에 저장 
    prev_height = curr_height
    
    #selenium 내용 ↑
    
    #################################################################
    #beautiful 내용 ↓
    
    
## html 파싱 -#find ,find_all, next_sibling , a[href]-> soup  명령어  
soup = BeautifulSoup(browser.page_source,"lxml")
data = soup.find("div",{"class":"mb-[calc(76px+env(safe-area-inset-bottom))]"})
a_list = data.find_all("a")
### 실제 출력
for a in a_list :
       title = a.find("p",{"class":"mb-4"}).get_text()
       print(title) # 제목 
       data2 =  a.find("div",{"class":"mp-2"})
       rank =  a.find("span",{"class":"typography-body-14-bold"}).get_text().strip()
       if rank !="후기":
           rank = float(rank)
       print(rank)  #평점 - 후기 :str 타입 ,float타입 
       
       rating = a.find("span",{"class":"typography-body-14-bold"}).next_sibling
       if rating !=None :
        rating =rating.get_text().strip()  # 평가수  (10) -str 타입 
        rating = int(rating[1:-1].replace(",","")) #10 -int타입  #괄호 없애는법
        print(rating) # 10
       price = a.find("span",{"class":"shrink-0"})
       if price !=None : 
           price = price.get_text().strip().replace(",","") # 천단위표시제거 
           price = int(price) 
           print(price)
       print("-"*30)

#x테스트 
# test= a_list[0].find("p",{"class":"mb-4"})
# print(test)
# print(len(a_list))

### 파일 저장
with open("w0514/ya1.html","w",encoding="utf-8") as f:
    f.write(soup.prettify()) # html파일저장
### 프로그램 종료
input("프로그램 종료시 엔터")
