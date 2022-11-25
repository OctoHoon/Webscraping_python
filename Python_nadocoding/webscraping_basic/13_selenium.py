# pip install selenium
# chrome version 확인 후, 버전에 맞는 크롬 드라이버 다운
# 크롬드라이버 압축 풀어서 chromedriver.exe 파일이 폴더 밖에 있도록

# 네이버 로그인 한 뒤, html 정보 가져와 쉽게 웹 스크래핑 할 수 있도록 하기

import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe") # 실행 경로와 같은 곳에 chromdriver.exe 있어서 괄호 안 채워도 됨. 아닌 경우 경로 정보 적어야 함

# 터미널에서 한 줄 씩 실행해 보는 것이 과정 보는 데 좋음

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3) # 자동입력 방지 때문에 입력 안 될 수 있어서 잠시 기다림

# 5. 로그인 실패한 경우 id 를 새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. 로그인 성공 후 html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 모든 탭 종료