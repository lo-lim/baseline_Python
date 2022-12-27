# 정규표현식을 이용한 문자열 검색에 사용되는 함수

# 함수            기능
#-----------------------------------------------------------------------------------
# match()       문자열의 처음부터 정규식과 매치되는지 검사한다.
# search()      문자열 전체를 검색하여 정규식과 매치되는지 검사한다.
# findall()     정규식과 매치되는 모든 문자열을 리스트로 리턴한다.
# finditer()    정규식과 매치되는 모든 문자열을 iterator객체로 리턴한다.

import re

# 영문자(a~z) 정규식 생성
# from sympy import primenu

p = re.compile('[a-z]+')

# 1. match()
# match() 함수는 정규식과 매치될때에는 match객체를 리턴하고
# 매치되지 않는 경우에는 None 을 리턴한다.
m1 = p.match('python')    # match='python'   #a-z까지안에 다 포함되기에 매치가 되어서 출력
print(m1)
m2 = p.match('Python')   # None  #앞에 대문자 P라서 매치가 안됨. 앞 부분부터 조건에 안 맞으면 그냥 바로 매치가 안 된다고 여기고 None 출력
print(m2)
m3 = p.match('pythoN')    # match='pytho' #맨 뒤에 대문자 N이라서 그걸 제외하고 pytho가 출력. 즉 match는 첫 번째 문자부터 적용이 되는 것만 출력
print(m3)
m4 = p.match('pyThon')
print(m4)                       # match='py'
m5 = p.match('3 python')
print(m5)                       # None
print('----------------------------------------------')

# 2. search()      # 전체 문자열까지 포괄적으로 봐서 앞 부분부터 매치가 안 되더라도 뒷 부분에 매치가 되는 부분이 있으면 매치가 된다고 여기고 조건에 해당되는 걸 다 출력
print('search()함수')
s1 = p.search('python')
s2 = p.search('Python')
s3 = p.search('pythoN')
s4 = p.search('pyThon')
s5 = p.search('3 python')
print(s1)                   # match='python'
print(s2)                   # match='ython'
print(s3)                   # match='pytho'
print(s4)                   # match='py'  #중간에 대문자가 있는 경우에는 앞에 py까지만 출력
print(s5)                   # match='python'
print('----------------------------------------------')

# 3. findall() 함수  #매치되는 값을 list로 받아서 출력함
result1 = p.findall('life is too short')
print(type(result1))        # 'list'
print(result1)              # ['life', 'is', 'too', 'short']

result2 = p.findall('Life is tOo shorT')     #a-z에 해당하는 식들만 출력함
print(result2)              # ['ife', 'is', 't', 'o', 'shor']
print('-----------------------------------------------------')

# 4. finditer() 함수
result3 = p.finditer('life is too short')
print(type(result3))        # 'callable_iterator'
print(result3)              # <callable_iterator object at 0x0000020A8F53DC48>

for r in result3:
    print(r)

result4 = p.finditer('Life is tOo shorT')
for r in result4:
    print(r)

