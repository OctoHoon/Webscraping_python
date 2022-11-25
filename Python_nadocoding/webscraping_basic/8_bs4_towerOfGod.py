# 네이버 웹툰 회차들의 제목과 링크 스크래핑. 평점 구하기.

import requests

from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=648419&weekday=mon"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"] # 속성 가져올 때는 대괄호
# print(title)
# print("https://comic.naver.com" + link)

# 만화 제목, 링크 가져오기

# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title)
#     print(link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})

for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))


# 컴파일러 언어/ 인터프리터 언어
# 컴파일 방식: 코드를 컴퓨터가 알아 들을 수 있도록 변환 한 뒤 실행
# 인터프리팅 방식: 한 줄 씩 바로 실행 가능
# 파이썬은 인터프리터 언어여서 터미널에 'python' 입력 후 한줄씩 실행 가능
# 코드를 터미널에 C+V 하려면 마우스 우클릭
# exit()로 실행중이던 터미널 종료

# beautifulsoup Documentation 에서 bs4 공부 가능!