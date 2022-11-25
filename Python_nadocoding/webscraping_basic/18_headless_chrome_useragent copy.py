# selenium 이용하면 웹 브라우저 띄워서 일일이 확인해야 되는데, 이를 백그라운드에서 진행해서 속도를 높이는 방법

from json import detect_encoding
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080") # 눈에 보이지는 않지만 백그라운드에서 도는 윈도우의 사이즈 정의

# headlessChrome 방지! user agent 적용!
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")


browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/103.0.0.0 Safari/537.36

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
# 결과
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# HeadlessChrome/103.0.5060.114 Safari/537.36

# 서버 입장에서는 HeadlessChrome의 접속 막을 수 있음. 이를 방지하기 위해 options.add_argument("user-agent= ...") 추가
browser.quit()