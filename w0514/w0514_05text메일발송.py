import smtplib
from email.mime.text import MIMEText

smtpName = "smtp.naver.com"
smtpPort = 587

#중요정보 
recvEmail = "km24778@gmail.com"
password ="YGHQTRQ6E7FU" ## 네이버 로그인 비밀번호를 입력해도 되지만 , 파일이 노출되면 
text = "날씨정보 오늘날씨:맑음, 내일날씨:흐리고 비" 

msg  = MIMEText(text)
msg['Subject'] = "웹스크래핑 이메일 보내기"
msg['From'] = "km24777@naver.com" # 네이버주소메일이 아니면에러 
msg['To'] = recvEmail 

s= smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("km24777@naver.com",password)
#보내는 주소가 네이버 메일이 아니면 에러처리  (보내는주소,받는주소 , ~ )
s.sendmail("km24777@naver.com",recvEmail,msg.as_string()) 
s.close()

print("메일발송 완료") 



