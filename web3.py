# web3.py
#웹서버에 요청
import urllib.request
#문자열 검색해서 크롤링
from bs4 import BeautifulSoup
#정규표현식
import re

#문자열 리턴
#웹브라우저의 헤더 셋팅
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#페이징 처리가 추가되는 경우
for i in range(1,11):
    url = "http://www.todayhumor.co.kr/board/list.php?table=bestofbest" + str(i) #정수니까 str함수로 감싸주기!
    print(url)
    req = urllib.request.Request(data, headers = hdr)
    data = urllib.request.urlopen(req).read()
    page = data.decode('utf-8', 'ignore')
    soup = BeautifulSoup(data, "html.parser")
    #클리앙중고장터에서 가져옴

    #<td class="subject">
    #   <a href="/board/view.php">한국에서 이름을 잃어버린 이탈리아 과자</a>
    #</td>

    lst = soup.find_all("td", attrs = {"class":"subject"})
    for item in lst:
        title = item.find("a").text
        if re.search("중국", title):
            print(title.strip())

