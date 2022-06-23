# web1.py
from bs4 import BeautifulSoup

# 페이지 로딩
page = open("c:\\work\\test01.html", "rt", encoding = "utf-8").read()
# 검색이 용이한 객체 (html에서 데이터를 빼올게~)
soup = BeautifulSoup(page, "html.parser")
# 문자를 그대로 보기
# print(soup.prettify())

# <p> 태그 전체를 검색
# print(soup.find_all("p"))


# 첫 번째 <p> 검색
# print(soup.find("p"))

# 조건이 있는 경우 : <p class=outer-text> 
# 키워드 인자를 변수 명으로 쓰면 안되니까 충돌나지 말라고 "_" 붙이기
# print(soup.find_all("p", class_="outer-text"))

# id 속성으로 검색
# print(soup.find_all(id="first"))

# 문자열만 리턴 (태그 다 상관 없고 내용만 불러오기)
for item in soup.find_all("p"):
    title = item.text
    title = title.replace("\n","")
    print(title.strip())
# 스트립은 빈칸 제거

