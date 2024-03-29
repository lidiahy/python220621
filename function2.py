# function2.py

# 함수 정의(LGB 이름 해석 규칙) local global built-in
x = 2
def func(a):
    return a+x

# 호출
print(func(1))

# 함수 정의
def func2(a):
    x = 1
    return a+x

# 호출
print(func2(a))

# 함수의 기본값
def times(a = 10, b = 20):
    return a*b

# 호출
print(times())
print(times(5))
print(times(5,6))

# 키워드 인자(파라미터 명 명시)
def connectURI(server, port):
    strURL = "http://"+server+":"+port
    return strURL

connectURI("credu.com", "80" )
connectURI(port="8080", server="credu.com")

# 순서 바꿔도 무방~

# 가변인자 함수
def union(*ar):
	result = []
	for item in ar:
		for x in item:
			if x not in result:
				result.append(x)
	return result

# 호출
union("HAM", "EGG")
union("HAM", "EGG", "SPAM")

# 정의되지 않은 인자(필수, 옵션)
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" +user[key] + "&"
    return strURL

# 호출
userURIBuilder("credu.com", "8080", id = "kim", passwd = "1234")
userURIBuilder("test.com", "8080", id = "kim", passwd = "1234", name = "Bongsoo")

# 람다 함수 (간결한 함수 정의)
g = lambda x,y: x*y
g(2,3)
print(g(3,4))
print(g(4,5))
print((lambda x:x*x)(3))
(lambda x:x*x)(3)
print(globals())
