# 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오

# [조회 조건]
# 1. http://daum.net 접속
# 2. '송파 헬리오시티' 검색
# 3. 다음 부동산 부분에 나오는 결과 정보

# [출력 결과]
# =========== 매물 1 =============
# 거래: 매매
# 면적: 84/59 (공급/전용)
# 가격: 165,000 (만원)
# 동: 214동
# 층: 고/23
# =========== 매물 2 =============

# ....

# 다음 사이트 바뀌어서 네이버로 해보겠음

from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.naver.com/")

browser.find_element_by_id("query").send_keys("송파 헬리오시티")
browser.find_element_by_id("search_btn").click()

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

houses = soup.find_all("ul", attrs={"class":"list_detail"})

for idx, house in enumerate(houses):
    print("=========== 매물 {} =============".format(idx+1))
    print("공급/전용: {}".format(house.find_all("span", attrs={"class":"dsc"})[0].get_text()))
    print("세대수: {}".format(house.find_all("span", attrs={"class":"dsc"})[1].get_text()))
    print("관리비: {}".format(house.find_all("span", attrs={"class":"dsc"})[2].get_text()))
    print("공시가격: {}".format(house.find_all("span", attrs={"class":"dsc"})[3].get_text()))