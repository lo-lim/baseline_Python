# split() : 문자열을 특정 구분기호로 분리 시키는 함수
# split('구분기호')

s = 'Life is too short'
result = s.split(' ')       # 공백으로 파싱(parsing)
print(type(result))         # <class 'list'> #문자열이 구분기호 ' ' (공백)을 만나서 list가 됨
print(result)               # ['Life', 'is', 'too', 'short']

s1 = 'python:java:oracle:jsp:spring:tensorflow'
result1 = s1.split(':')     # 콜론(:)으로 파싱
print(result1)              # ['python', 'java', 'oracle', 'jsp', 'spring', 'tensorflow']

for i in result1:
    print(i)

#즉 구분기호를 기준으로 분리가 됨.
#for는 자료구조와 결합할 수 있다고 했는데 result1이 list라는 자료구조형태이니 for과 결합한 것.