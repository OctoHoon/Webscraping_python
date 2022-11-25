# 웹 스크래핑을 이용하여 나만의 비서를 만드시오

# [조건]
# 1. 네이버에서 오늘 서울의 날씨정보를 가져온다
# 2. 헤드라인 뉴스 3건을 가져온다
# 3. IT 뉴스 3건을 가져온다
# 4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다

# [출력 예시]

# [오늘의 날씨]
# 흐림, 어제보다 00도 높아요
# 현재 00도 (최저 00도 / 최고 00도)
# 오전 강수확률 00% / 오후 강수확률 00%

# 미세먼지 00ug/m3 좋음
# 초미세먼지 00ug/m3 좋음

# [헤드라인 뉴스]
# 1. 무슨 무슨 일이...
# (링크 : https://...)
# 2.
# 3.

# [IT 뉴스]
# 1. 무슨 무슨 일이...
# (링크 : https://...)
# 2.
# 3.

# [오늘의 영어 회화]
# (영어 지문)
# ....__annotations__
# (한글 지문)
# ...

import requests
from bs4 import BeautifulSoup
import re

def create_soup(url):
    headers = {"accept-language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7","accept-encoding":"gzip, deflate, br","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-mode":"document","sec-fetch-mode":"navigate", "sec-fetch-site":"none","sec-fetch-user":"?1","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EC%A0%84+%EB%82%A0%EC%94%A8&tqi=hWaQjwp0YihssvWTheKssssssyw-325416"
    soup = create_soup(url)

    # 흐림, 어제보다 00도 높아요
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    # 현재 00도 (최저 00도 / 최고 00도)
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace("온도", "").strip()
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text()
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text()
    # 오전 강수확률 00% / 오후 강수확률 00%
    am_rain = soup.find("li", attrs={"class":"week_item today"}).find_all("span", attrs={"class":"weather_left"})[0].get_text().strip()
    pm_rain = soup.find("li", attrs={"class":"week_item today"}).find_all("span", attrs={"class":"weather_left"})[1].get_text().strip()

    # 미세먼지 00ug/m3 좋음
    # 초미세먼지 00ug/m3 좋음
    dust_1 = soup.find("ul", attrs={"class":"today_chart_list"}).find_all("li")[0].find("span").get_text()
    dust_2 = soup.find("ul", attrs={"class":"today_chart_list"}).find_all("li")[1].find("span").get_text()
    # 출력
    print(cast)
    print(curr_temp)
    print(min_temp)
    print(max_temp)
    print("강수량: " + am_rain)
    print("강수량: " + pm_rain)
    print("미세먼지: " + dust_1)
    print("초미세먼지: " + dust_2)

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)

    headlines = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3) # 3개 까지 찾기

    for idx, headline in enumerate(headlines):
        a_idx = 0
        img = headline.find("img")
        if img:
            a_idx = 1 # img 태그가 있으면 1번째 a 태그의 정보를 사용

        print("{}. {}".format(idx + 1, headline.find_all("a")[a_idx].get_text().strip()))
        print("(링크: {})".format(headline.find_all("a")[a_idx]["href"]))

def scrape_hackers():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print()
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    print()
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())


if __name__ == "__main__":
    scrape_weather() # 파일을 직접 실행할 때만 호출 되도록! (다른 파일에서 호출될 경우 실행 안 됨)
    print()
    scrape_headline_news()
    print()
    scrape_hackers()