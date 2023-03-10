import re

#meta.py파일에서 정규 표현식을 안 하고 바로 식을 쓰는 방법으로 사용

m1 = re.match('[0-9]', '1234')   #[0-9]는 0에서 9사이이고 1234가 이 사이에 다 들어가 있는데 print(m1)을 하면 1234중에서 1만 출력
print(m1)                           # match='1'
print(m1.group())                   # 1 : 매치된 문자열 반환  #바로 1이라는 값 출력

m2 = re.match('[0-9]', 'abc') #0-9까지의 숫자 중에서 abc가 없기에 매치가 되지 않음
print(m2)                           # None : 매치되는 문자 없음

m3 = re.match('[0-9]+', '1234')  #1234를 다 출력하고 싶으면 뒤에 +를 붙이면 된다.  # +은 한 번이상 반복이 되면 매치가 되는건데 1234가 0-9에서 다 한 번 이상 반복이니까 1234를 다 매치
print(m3)                           # match='1234'
print(m3.group())                   # 1234

# 맨 앞에 공백이 있는 경우
m4 = re.match('[0-9]+', ' 1234')      #1234 앞에 공백이 있는 경우에는 매치가 되지 않는 걸로 인식함
print(m4)                           # None

# 맨 앞에 공백이 오는 경우에는 \s를 이용해야 한다.  #\s를 하면 앞에 공백이 있어도 매치가 되는 걸로 출력한다.
m5 = re.match('\s[0-9]+', ' 1234')
print(m5)                           # match=' 1234'
print(m5.group())                   # 1234

# search()메소드는 문자열 전체를 검색하여 정규식과 매치되는지 검사한다.  #1234 앞에 공백이 있으면 match는 그냥 none으로 출력이 되는데 search는 처음에 공백이더라도 문자열 전체를 다 검색하기 때문에 매치가 된다고 출력
m6 = re.search('[0-9]+', ' 1234')
print(m6)                           # match='1234'
print(m6.group())                   # 1234

#match 함수는 처음에 문자부터만 비교를 하지만 search는 전체 문자까지를 보기 때문에 앞에 공백이 있어도 뒤에 알맞는 값이 있으면 매치가 된다고 여긴다.