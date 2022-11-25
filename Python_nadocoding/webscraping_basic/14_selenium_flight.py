from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

# 네이버 항공권 사이트 가는 날 선택이 링크에서 버튼으로 태그 종류가 바뀌워서 못 했음..

url = "https://flight.naver.com/flights/"
browser.get(url) # url 로 이동

# 가는 날 클릭
browser.find_element_by_link_text("가는 날").click()

# 로딩 기다리는 법 (특정 시간 동안 말고, 로딩 될 떄까지만 기다림)

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "-----")))
    # 성공했을 때 동작 수행
finally:
    browser.quit()

# 브라우저를 최대 10초간 기다림. 10 초 안에 입력한 조건 성립되면 (xpath 값에 해당하는 엘리먼트가 있으면) 계속 진행.
