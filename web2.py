# web2.py
import urllib.request
from bs4 import BeautifulSoup

# 파일로 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding = "utf-8")
# 동적으로 주소 생성

# 웹페이지의 실행결과를 문자열로 받기
url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page="
data = urllib.request.urlopen(url)
# 검색할 객체 생성
soup = BeautifulSoup(data, "html.parser")
cartoons = soup.find_all("td", class_="title")
print("개수:{0}".format(len(cartoons)))
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)


for item in cartoons:
    title = item.find("a").text
    print(title.strip())

f.close()
