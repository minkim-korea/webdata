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
#메일관련 import 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders 

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

#1.csv 파일생성 (import csv 있는지확인)  
f = open("w0515/news.csv","w",encoding="utf-8-sig",newline='') # newline 엔터키 안쳐지게하는거 
writer =csv.writer(f)

title = ['언론사','기사제목']
writer.writerow(title) # csv 리스트 저장 


### 1. 네이버 접속
url = "https://news.naver.com/main/ranking/popularDay.naver"
browser.get(url)
#html파싱 
soup = BeautifulSoup(browser.page_source,"lxml")

#언론사별 랭킹 뉴스 전체찾기
data = soup.find("div",{"class":'rankingnews_box_wrap'})
# 랭킹뉴스 리스트 12개 찾기 
rNews= data.find_all("div",{"class":"rankingnews_box"})

# 12번 반복해서 가져옴. 
for r in rNews:
    
    # 언론사 이름 
    newsName = r.find("strong",{"class":"rankingnews_name"}).get_text().strip()
    print(newsName)
    ## 기사제목 
    newsContent = r.find("a",{"class":"list_title"}).get_text().strip()
    print(newsContent)
    writer.writerow([newsName,newsContent]) # 12번 적힌거 넣는거 
## 파일생성 완료     
f.close()
#파일생성동안 잠시 대기 
time.sleep(2)

####메일 발송 ###############################

#중요부분 
recvMail = "km24777@naver.com" #받는사람 주소 
password ="8DC24YQR2TQB" ## 네이버 로그인 비밀번호를 입력해도 되지만 , 파일이 노출되면 

## MIME 객체화 
msg = MIMEMultipart("alternative")
# 내용부분
text ="""<h2>랭킹뉴스 기사 모음 </h2>
<img src ='https://mail.naver.com/read/image/original/?mimeSN=1747271390.582508.155.46848&offset=1762&size=4808542&u=km24777&cid=971340a683273d3b5154e17ad6fe46bd@cweb004.nm&contentType=image/jpeg&filename=1747271388807.jpeg&org=1'>

"""# html 문구도 가능 이미지보낼때 웹주소이미지로 보내야 보임  
part2 = MIMEText(text,"html")  # html 문구도 넣을수있음 
msg.attach(part2)
msg['From'] = "km24777@naver.com"
msg['To'] = recvMail
msg['Subject'] ="언론사별 랭킹뉴스를 보냅니다."

##파일첨부 
part = MIMEBase('application',"octet-stream")
## 파일읽어오기 
with open("w0515/news.csv","rb")as f :
    #part 담기 
    part.set_payload(f.read())
#파일첨부할수 있는 형태로 인코딩 
encoders.encode_base64(part)
## header 정보 - 파일이름을 변경해야됨
part.add_header('Content-Disposition','attachment',filename='news.csv')
msg.attach(part)

s =smtplib.SMTP("")
s= smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("km24777@naver.com",password)
#보내는 주소가 네이버 메일이 아니면 에러처리  (보내는주소,받는주소 , ~ )
recvMails = 'km24777@naver.com'
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
