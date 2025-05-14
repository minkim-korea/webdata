import requests
from bs4 import BeautifulSoup

### fly1.html 불러오기 
with open("w0513/fly1.html","r",encoding="utf8") as f :
    soup = BeautifulSoup(f,"lxml")

datas = soup.find_all("div",{"class":"domestic_Flight__8bR_b"})
datas_list=[] # 리스트 정렬하기위해서 사용하기위해 생성 
for data in datas:
    ## 항공사이름 
    airline = data.find("b",{"class":"airline_name__0Tw5w"}).get_text().strip()
    print(airline)
    
    times = data.find_all("b",{"class":"route_time__xWu7a"})
    startTime =times[0].get_text() # 출발시간 
    print(startTime)
    endTime =times[1].get_text()  # 도착시간 
    print(endTime)
    price= data.find("i",{"class":"domestic_num__ShOub"}).get_text().strip().replace(",","") # 가격 
    price= int(price)
    print(price)
    print("-"*50)  
    datas_list.append([airline,startTime,endTime,price])   # 튜플은 수정이 안되고 리스트는 수정가능 


###최저가 LIST정렬 
dd_list =sorted(datas_list,key = lambda x:x[3]) #순차정렬  역순은-> reverse=True
print(dd_list)
# 최소값이 몇번째인지 찾고 출력해보기 






# ### 항공사 , 출발시간 ,도착시간 ,금액 출력해보기  (나혼자해본거)
# for i in range(1,317): 
#     air = soup.find_all("span",{"class":"airline_text__WWkbY"})
#     name = air[i].find("b")
#     print(name.get_text().strip())  # 항공사 
    
#     hours = soup.find_all("div",{"class":"route_Route__HYsDn"})
#     hourss = hours[i].find_all("b")
#     print(hourss[0].get_text().strip())  #출발시간 
#     print(hourss[1].get_text().strip())  #도착시간 
    
#     price2 = soup.find_all("div",{"class":"domestic_prices__WBiv_"})
#     price = price2[i].find("i",{"class":"domestic_num__ShOub"})
#     print(price.get_text().strip())
#     print("-"*20)
    
    
    