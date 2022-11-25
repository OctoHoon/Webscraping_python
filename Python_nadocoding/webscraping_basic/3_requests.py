import requests
res = requests.get("http://google.com")
#res = requests.get("http://nadocoding40.tistory.com") # 없는 사이트 또는 접근 금지된 사이트
res.raise_for_status() # 문제가 생길 경우 바로 오류를 내서 프로그램 종료
# print("응답코드 :", res.status_code) # 200이면 정상, 200 아니면 사이트 접근 불가

# if res.status_code == requests.codes.ok: # 200 과 동일한 값
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text)) # html 문서 텍스트 가져옴. 글자 수 출력

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)