import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders 

### 임시 패스워드는 : aaa1111 
### 자신에게 보내기 
### onulee@naver.com 




####메일 발송 ###############################

#중요부분 
recvMail = "km24777@naver.com" #받는사람 주소 
password ="8DC24YQR2TQB" ## 네이버 로그인 비밀번호를 입력해도 되지만 , 파일이 노출되면 

## MIME 객체화 
msg = MIMEMultipart("alternative")
# 내용부분
text ="""
<html xmlns="http://www.w3.org/1999/xhtml" lang="ko" xml:lang="ko">
<head>
<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<title> 비밀번호 발송 </title>


</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" style="margin:0; padding:0; font:normal 12px/1.5 돋움;">


<table width="700" cellpadding="0" cellspacing="0" align="center">
<tr>
	<td style="width:700px;height:175px;padding:0;margin:0;vertical-align:top;font-size:0;line-height:0;">
		<img src ='https://mail.naver.com/read/image/original/?mimeSN=1747272969.700540.164.55040&offset=1942&size=4808542&u=km24777&cid=d8cb25f76b5fda595a5c874cc82b58ba@cweb017.nm&contentType=image/jpeg&filename=1747272946078.jpeg&org=1'>					
	</td>
</tr>
<tr>
	<td style="width:700px;height:78px;padding:0;margin:0;vertical-align:top;">
		<p style="width:620px;margin:50px 0 40px 38px;text-align:center;font-size:0;line-height:0;"><img src="../images/email/img_txt_password01.jpg" alt="원두커피의 名家, JARDIN 임시 비밀번호가 발급되었습니다." /></p>
	</td>
</tr>
<tr>
	<td style="width:700px;height:196px;padding:0;margin:0;vertical-align:top;">
		<table width="618" height="194" cellpadding="0" cellspacing="0" align="center" style="margin:0 0 0 40px;border:1px #d9d9d9 solid;">
		<tr>
			<td style="width:618px;height:194px;padding:0;margin:0;vertical-align:top;font-size:0;line-height:0;background:#f9f9f9;">
				<p style="width:620px;margin:30px 0 0 0;padding:0;text-align:center;"><img src="../images/email/img_txt_password02.jpg" alt="JARDIN에서 비밀번호 찾기를 요청하셨습니다." /></p>
				<p style="width:620px;margin:10px 0 0 0;padding:0;text-align:center;color:#888888;font-size:12px;line-height:1;">아래의 PASSWORD는 임시 PASSWORD이므로 홈페이지 로그인 후 다시 수정해 주십시오.</p>
				<p style="width:620px;margin:28px 0 0 0;padding:0;text-align:center;color:#666666;font-size:12px;line-height:1;"><strong>임시 패스워드 : <span style="color:#f7703c;line-height:1;">aaa1111</span></strong></p>
				<p style="width:620px;margin:30px 0 0 0;padding:0;text-align:center;color:#888888;font-size:12px;line-height:1.4;">쟈뎅샵에서는 고객님께 보다 나은 서비스를 제공하기 위해 항상 노력하고 있습니다.<br/>앞으로 많은 관심 부탁드립니다.</p>
			</td>
		</tr>
		</table>	
	</td>
</tr>
<tr>
	<td style="width:700px;height:120px;padding:0;margin:0;vertical-align:top;">
		<p style="width:700px;margin:30px 0 50px 0;text-align:center;"><a href="#"><img src="../images/email/btn_jardin.jpg" alt="JARDIN 바로가기" /></a></p>
	</td>
</tr>
<tr>
	<td style="width:700px;height:50px;padding:0;vertical-align:top;font-size:0;line-height:0;text-align:center;">
		<img src="../images/email/img_email_bottom.jpg" alt="" />
	</td>
</tr>
<tr>
	<td style="width:700px;height:140px;padding:0;margin:0;vertical-align:top;background-color:#5a524c;">
		<p style="width:620px;margin:20px 0 0 40px;padding:0;text-align:center;line-height:1.5;color:#b2aeac;">메일수신을 원치 않으시는 분은 로그인 후. <span style="color:#ffffff">메일 수신 여부</span>를 변경해주시기 바랍니다.<br/>IF YOU DO NOT WISH TO RECEIVE EMAILS FROM US, PLEASE LOG-IN AND UPDATE<br/> YOUR MEMBERSHIP INFORMATION.</p>

		<p style="width:620px;margin:15px 0 0 40px;padding:0;text-align:center;line-height:1.5;color:#b2aeac;"><span style="color:#ffffff">본 메일에 관한 문의사항은 사이트 내 고객센터를 이용해주시기 바랍니다.</span><br/>COPYRIGHT ©  2014 JARDIN ALL RIGHTS RESERVED.</p>
	</td>
</tr>
</table>






<img src ='https://mail.naver.com/read/image/original/?mimeSN=1747272969.700540.164.55040&offset=4810780&size=4805124&u=km24777&cid=835e3e736a21b67c80f593cbd42a276@cweb008.nm&contentType=image/jpeg&filename=1747272960596.jpeg&org=1'> <br>
<img src ='https://mail.naver.com/read/image/original/?mimeSN=1747273015.103996.157.34560&offset=1915&size=4766834&u=km24777&cid=d34e23876abab532b688bbd63f5ac@cweb010.nm&contentType=image/jpeg&filename=1747272980339.jpeg&org=1'>

<img src ='https://mail.naver.com/read/image/original/?mimeSN=1747273015.103996.157.34560&offset=4769046&size=4769776&u=km24777&cid=877ac3bb6aea6cc88bb8894d4e4cfb58@cweb015.nm&contentType=image/jpeg&filename=1747272995716.jpeg&org=1'> <br>
<img src ='https://mail.naver.com/read/image/original/?mimeSN=1747273015.103996.157.34560&offset=9539119&size=4757162&u=km24777&cid=a255b7dd7a17ba8eda52b7337f19956e@cweb017.nm&contentType=image/jpeg&filename=1747273005615.jpeg&org=1'>

"""# html 문구도 가능 이미지보낼때 웹주소이미지로 보내야 보임  
part2 = MIMEText(text,"html")  # html 문구도 넣을수있음 
msg.attach(part2)
msg['From'] = "km24777@naver.com"
msg['To'] = recvMail
msg['Subject'] ="임시 비밀번호가 발급되었습니다.."

s =smtplib.SMTP("")
s= smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("km24777@naver.com",password)

#보내는 주소가 네이버 메일이 아니면 에러처리  (보내는주소,받는주소 , ~ )
recvMails = ['km24777@naver.com','km24778@gmail.com ']
for recvMail in recvMails:
    s.sendmail("km24777@naver.com",recvMail,msg.as_string()) 
s.close()




print("메일발송 완료")


