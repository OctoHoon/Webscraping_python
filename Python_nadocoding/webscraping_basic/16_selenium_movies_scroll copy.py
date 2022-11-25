# 동적 페이지에서 크롤링하기 : selenium 필요!
# 구글 무비에서 할인되는 영화 정보만 스크래핑!

from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/search?q=%EB%A1%9C%EB%A7%A8%EC%8A%A4&c=movies"
browser.get(url)

# 셀레니움에서 자바스크립트 코드 실행 가능
# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 2160)")

# 화면 가장 아래로 스크롤 내리기 (현재 예시는 한번만 로딩 되지만 스크롤 할 때마다 계속 되는 경우에 사용)
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    
    prev_height = curr_height

print("스크롤 완료")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"ULeU3b"}) # "class" : ["". ""] 도 가능. 리스트 형식으로 조건 맞는 것 전부 찾음
print(len(movies))

for movie in movies[3:]: # 0,1,2 는 앱 및 게임, 영화 , 도서 버튼임
        title = movie.find("div", attrs={"class":"Epkrse"}).get_text()

        # 할인 전 가격
        original_price = movie.find("span", attrs={"class":"SUZt4c P8AFK"})
        if original_price:
            original_price = original_price.get_text()
        else:
            # print(title, " <할인되지 않은 영화 제외>")
            continue
        
        # 할인된 가격
        price = movie.find("span", attrs={"class":"VfPpfd VixbEe"}).get_text()

        # 링크
        link = movie.find("a", attrs={"class":"Si6A0c ZD8Cqc" })["href"]
        # 올바른 링크 https://play.google.com + link

        print(f"제목 : {title}")
        print(f"할인 전 금액 : {original_price}")
        print(f"할인 후 금액: {price}")
        print("링크 : ", "https://play.google.com" + link)
        print("-" * 120)

browser.quit()
