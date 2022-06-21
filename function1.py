# function1.py
# 함수를 정의
def times(a,b):
    return a+b, a*b

# 함수를 호출
result = times(3, 4)
print(result)

# debugging 하려면 옆에 "실행 및 디버그"실행해야해
# 처음 해야하는게 launch.json 파일 만들기
# 디버깅 결과 config 나오는거는 dict와 유사한데, 이거는 웹상 dict로 인식하면 됨(사실 json)

# 라인넘버 옆 클릭하면 중단점 생성(red ball): 디버깅할 때 중단되는 점

# 불변형석인 경우
a = 1.2
print(id(a))
a = 2.3
print(id(a))

print("가변형식")
lst = [1,2.3]
print(id(lst))
lst.append(4)
print(id(lst))

# 참조를 복사 전달
def change(x):
    x[0] = "H"

# 호출
wordlist = ["J", "A", "M"]
change(wordlist)
print("함수 호출후:", wordlist)

def change(x):
    # 복사본(deep copy)
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부:", x1)

# 교집합 함수(디버깅 연습)
def intersect(prelist, postlist):
    # 지역변수로 교집합 문자를 저장
    result = []
    # H(0) | A(1) | M(2)
    for x in prelist:
        # x라는 글자가 postlist에 포함 && x가 아직 result에 없다
        if x in postlist and x not in result:
            result.append(x)
    return result

# 함수 호출
print(intersect("HAM", "SPAM"))

def times(a=10, b=20):
    return a*b

times()
times(5)

