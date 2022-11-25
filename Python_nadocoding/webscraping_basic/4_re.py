# # regular expression 정규식 표현
# 주민등록번호
# 990202-1411111  O
# abcdef-1111111  X

# 이메일 주소
# sakonghoon@naver.com       O
# sakonghoon@fdasf@dafd.com  X

# 차량 번호
# 11가 1234  O
# 123가 1234 O

# IP 주소
# 192.168.0.1            O
# 1000.2000.3000.4000    X

import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, ...

p = re.compile("ca.e") 
# . (ca.e): 하나의 문자를 의미 > care, cafe, case (O)| caffe (X)
# ^ (^de): 문자열의 시작 > desk, destination (O)| fade (X)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)

def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 입력받은 문자열
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작과 끝 index
    else:
        print("매칭되지 않음")

# m = p.match("careless") # match: 주어진 문자열의 처음부터 일치하는지 확인하기 때문에 매칭이 됨
# print_match(m)
# print(m.group()) # 매치되지 않으면 에러가 발생

# m = p.search("good care") # 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("careless cafe good care") # findall: 일치하는 모든 것을 리스트 형태로 반환
# print(lst)


# [정리]

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 반환

# 원하는 형태: 정규식
# . (ca.e): 하나의 문자를 의미 > care, cafe, case (O)| caffe (X)
# ^ (^de): 문자열의 시작 > desk, destination (O)| fade (X)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)

# [더 공부하고 싶으면]
# w3schools.com > python > Reg Ex
# python re (docs.python.org)