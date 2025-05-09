import requests
from bs4 import BeautifulSoup
import csv # csv 파일 저장 

# html파일을 읽어와서 파일html,css 형태로 파싱
with open("w0509/notice_list.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
# print(stable.tr.)
ff = open("w0509/list.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(ff) # csv파일 list 타입 저장

#### 상단, 내용부분 
trs= soup.table.find_all("tr")
#print(len(trs))
for i,tr in enumerate(trs):
    fileName=[]
    if i==0: #상단 타이틀 
        ths = soup.table.find_all("th")
        for th in ths:
            print(th.get_text(),end="\t")
            fileName.append(th.get_text())
            
        writer.writerow(fileName)  #상단타이틀 list타입으로 저장 
        print()
        continue
    #내용부분
    tds = tr.find_all("td")
    for td in tds:
        print(td.get_text(),end="\t")
        fileName.append(td.get_text())
    print()
    writer.writerow(fileName)  # 놰용부분 list타입으로 저장 

print("파일저장 완료")