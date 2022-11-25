# url 종류
# GET 방식: url의 ? 뒤에 변수+값 이 있는 형태. 큰 데이터 보내지 못 함.
# https://www.coupang.com/np/search?minprice=100&maxprince=10000&page=2
# 편리하게 url을 약간 조작해서 다른 페이지에 접근 가능. 쿠팡의 경우 get 방식이어서 쉽게 웹스크래핑 가능.
# POST 방식: 좀 더 보안이 좋음. 개인정보 담은 페이지 등. 
# 쿠팡은 헤더를 구체적으로 제시 해줘야 접근 가능.

import requests
import re
from bs4 import BeautifulSoup


headers = {"accept-language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7","accept-encoding":"gzip, deflate, br","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-mode":"document","sec-fetch-mode":"navigate", "sec-fetch-site":"none","sec-fetch-user":"?1","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}


url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# print(res.text)

items = soup.find_all("li", attrs={"class":re.compile("^search-product")}) # search-product 로 시작하는 클래스. (광고 있고 없고에 따라 클래스 이름 달라서)
# print(items[0].find("div", attrs={"class":"name"}).get_text())
for item in items:

    # 광고 제품은 제외 (광고 태그가 붙어있으면 제외)
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print(" <광고 상품 제외합니다>")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명

    # 애플 제품 제외
    if "Apple" in name:
        print(" <Apple 상품 제외합니다>")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격정보

    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"}) # 평점
    if rate:
        rate = rate.get_text()
    else:
        print(" <평점 없는 상품 제외합니다>")
        continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 리뷰 수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
    else:
        print(" <평점 수 없는 상품 제외합니다>")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)