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
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders 
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# # 브라우저 실행
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() # 창 최대화

# ff = open("w0514/news.csv","a",encoding="utf-8-sig",newline="")
# writer = csv.writer(ff)

# url = "https://news.naver.com/main/ranking/popularDay.naver"
# browser.get(url)

# def newsSearch(nXpath):
#     titles = []
#     time.sleep(1)
#     # 뉴스부분 클릭
#     browser.find_element(By.XPATH,nXpath).click()
#     # 웹스크래핑시작
#     soup = BeautifulSoup(browser.page_source,"lxml")
#     data = soup.find("div",{"class":"media_end_head_title"})
    
#     # 뉴스제목출력
#     title = data.find("span").get_text()
#     print(title)
#     titles.append(data.get_text().strip())
#     writer.writerow(titles)
#     # 뉴스내용출력
#     newssct = soup.find("article",{"id":"dic_area"})
#     print(newssct.get_text())
#     time.sleep(1)
#     titles.append(newssct.get_text().strip())
#     writer.writerow(titles)
#     time.sleep(1)
#     # 뒤로 가기
#     browser.back()
# for i in range(1,13):
#     ## 1. 뉴스 클릭
#     nXpath = f'//*[@id="wrap"]/div[4]/div[2]/div/div[{i}]/ul/li[1]/div/a'
#     newsSearch(nXpath)
    

# ff.close()
# print("종료")





#################################################메일
# #중요부분 
recvMail = "onulee@naver.com" #받는사람 주소 
password ="2ZXWNJ7U6GVW" ## 네이버 로그인 비밀번호를 입력해도 되지만 , 파일이 노출되면 

# ## MIME 객체화 
msg = MIMEMultipart("alternative")
# 내용부분
text ="네이버 랭킹 뉴스보냅니다"
part2 = MIMEText(text)
msg.attach(part2)
msg['From'] = "km24777@naver.com"
msg['To'] = recvMail
msg['Subject'] = "네이버 12개 랭킹 1위 뉴스를 보내드립니다. "

##파일첨부 
part = MIMEBase('application',"octet-stream")
## 파일읽어오기 
with open("w0514/news.csv","rb")as f :
    #part 담기 
    part.set_payload(f.read())
#파일첨부할수 있는 형태로 인코딩 
encoders.encode_base64(part)
## header 정보 
part.add_header('Content-Disposition','attachment',filename='stokc')
msg.attach(part)
password ="YGHQTRQ6E7FU"
s =smtplib.SMTP("")
s= smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("km24777@naver.com",password)
s.sendmail("km24777@naver.com",recvMail,msg.as_string()) 
s.close()

print("메일발송 완료")
##퀴즈 ######
# news.csv
# 신문사  / 기사 
# 뉴시스 ," ~ "
# 한국경제 ,'~' 
# 파일첨부 메일로 발송은 onulee@naver.com 으로 
# 제목 : 네이버 랭킹 뉴스보냄. 
# 내용 : 네이버 12개 랭킹 1위 뉴스를 보내드립니다. 
