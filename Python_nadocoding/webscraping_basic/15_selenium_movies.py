# 동적 페이지에서 크롤링하기 : selenium 필요!
# selenium with Python 으로 셀레니움 공부 가능!

import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/search?q=%EB%A1%9C%EB%A7%A8%EC%8A%A4&c=movies"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }
# 한글 언어로 된 페이지를 요청.

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ULeU3b"})
print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#     #f.write(res.text)
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력
#     # headers 에 한글로 된 페이지 요청하지 않으면 영어로 된 페이지가 나옴. 따라서 결과가 달라질 수 있음.


for movie in movies[3:]: # 0,1,2 는 앱 및 게임, 영화 , 도서 버튼임
        title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
        print(title)
        
