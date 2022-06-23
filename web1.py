# web1.py
from bs4 import BeautifulSoup

# 페이지 로딩
page = open("c:\\work\\test01.html", "rt", encoding = "utf-8").read()
# 검색이 용이한 객체 (html에서 데이터를 빼올게~)
soup = BeautifulSoup(page, "html.parser")
# 문자를 그대로 보기
print(soup.prettify())