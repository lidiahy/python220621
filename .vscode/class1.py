# class1.py
# 1) 클래스를 정의
class Person:
    # 생성자(초기화) 메서드
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

# 2) 인스턴스 생성
p1 = Person()
p2 = Person()

# 3) 메서드 호출
p1.print()
p2.name = "RafaelNadal"
p2.print()

# 런타임시에 변수 추가
# 통상 정적 언어에서는 title 변수 걸면 syntax error 발생
# 파이썬은 개발자가 필요해서 입력했겠거니~ 하고 말음
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)
