import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers) 
#res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)

# What is my user agent? : 접속하는 서버에 따라 다름
# 크롬에서 접속한 경우 이 컴퓨터는 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36
# user agent 값을 제공해 주면(헤더 정보 제공) 사이트에서 차단한 정보를 가져올 수 있음. 제대로 웹 스크래핑 가능