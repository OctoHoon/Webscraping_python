# pip install beautifulsoup4 (웹 스크래핑)
# pip install lxml (구문 분석 parser)
# parser? 컴파일러의 일부. 프로그램을 읽어 들여 문장 구조를 알아내는 구문 분석 행함
# from bs4 에러 났는데, 파이썬 인터프리터의 경로가 다른 버전으로 잘못 설정되어 있었음!

import requests

from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text()) # 글자만 추출
# print(soup.a) # soup 객체에서 처음으로 발견되는 a element 반환
# print(soup.a.attrs) # a element 의 속성 정보 출력
# print(soup.a["href"]) # a element 의 href 속성 '값' 정보 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # 네이버 웹툰 페이지의 '웹툰 올리기' 버튼 속성 찾은 뒤 찾아보기
# class 값이 Nbtn_upload 인 a element 를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"})) # 웹툰 올리기 버튼이 하나여서 태그 굳이 지정 안해도 됨
# class 값이 Nbtn_upload 어떤 element 를 찾아줘

# print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a) # a element 만 출력

# print(rank1.a.get_text())
# print(rank1.next_sibling.next_sibling) # 다음 element 로 이동. 개행 정보 때문에 2번 사용.
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling

# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li") # 조건에 해당하는(li 태그 기준으로) next_sibling 찾음. 개행정보 안 찾게 됨.
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="퀘스트지상주의-38화 니체가 말했지")
print(webtoon)