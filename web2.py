# web2.py
#웹서버에 요청
import urllib.request
#크롤링에 필요
from bs4 import BeautifulSoup

#웹서버에 요청해서 결과물을 문자열로 받기
#패키지명.모듈명.함수명
data = urllib.request.urlopen('https://comic.naver.com/webtoon/list.nhn?titleId=20853&amp;weekday=fri')
# 검색이 용이한 객체
soup = BeautifulSoup(data, "html.parser")

# <td class="title">
#     <a href="/webtoon/detail.nhn">마음의\ 소리 49화 <지혜></a>
# </td>

cartoons = soup.find_all("td", class_="title")
#첫번째만 슬라이싱(10개)
#cartoons[0],cartoons[1].....
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)

#반복구문
print("====반복구문====")
#파일로저장
f = open("c:\\work2\\webtoon.txt", "wt",encoding = "utf-8")
#한글이 들어갔으니까 인코딩 지정해줘야 안 깨짐
for item in cartoons:
    title = item.find("a").text
    print(title)
    f.write(title.strip() + "\n")

f.close() #까먹으면 안됨!
