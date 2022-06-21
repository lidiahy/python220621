# 람다 함수 (간결한 함수 정의)
g = lambda x,y: x*y
g(2,3)
print(g(3,4))
print(g(4,5))
print((lambda x:x*x)(3))
(lambda x:x*x)(3)
print(globals())