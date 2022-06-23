# db1.py
import sqlite3

# 연결 객체를 리턴받기 (일단 메모리에서 연습. 속도)
con = sqlite3.connect(":memory:")
# 커서 객체를 리턴받기
cur = con.cursor()
# 테이블(스키마)를 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
# 1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")
# 입력 파라미터 처리
name = "gildong"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))
# (name, phoneNumber) 튜플로 묶인 인스턴스가 한 번에 입력됨

# 여러 건을 입력
datalist = (("tom", "010-123"), ("dsp", "010-456"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

# 검색
#  cur.execute("select * from PhoneBook;")

#  for row in cur:
#     print(row)
# 튜플로 출력됨

#튜플이 싫으면
cur.execute("select * from PhoneBook;")

# for row in cur:
#     print(row[0] + "," +  row[1])
    
# 검색 메서드 사용
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
print(cur.fetchall())

# 레코드 포인터가 가리키는 위치부터 데이터 끝까지가 1줄 남은거

print("데이터 재로드")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())