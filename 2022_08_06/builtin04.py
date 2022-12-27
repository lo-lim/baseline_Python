# 내장 함수 : format()

# format(데이터, 서식형식)
print(4)
print(format(4, '10d'))          # 정수를 출력하는 10자리
#10d는 정수를 출력하는 10개의 자리를 만들고 출력하라는 의미, d는 정수
print(format(4.3, '10.3f'))      # 실수를 출력하는 전체 10자리, 소숫점 이하 3자리
print(format(42.195678,  '.3f')) # 소숫점 3자리까지 출력 : 42.196
print(format('안녕하세요', 's')) #s는 문자형태로 출력하라는 의미
print(format(42.195678,  '.2f')) # 소수점 2자리까지 출력

# {숫자}와 format()함수를 이용한 데이터 매핑
print('{0} is {1}'.format('Python', 'fun'))     # Python is fun
print('{} is {}'.format('Python', 'fun'))       # Python is fun
print('{1} is {0}'.format('Python', 'fun'))     # fun is Python
# 위치에 맞게 각각의 숫자와 값들을 이어서 출력할 때 숫자 순서대로 출력

print(format(5, '7d'))
print(format(4.55, '7.4f'))

# 키보드로 입력한 문자를 format()함수로 출력
name = input('이름을 입력하세요?')
job = input('직업을 입력하세요?')

print('{0} is a {1}'.format(name, job))     # 홍길동 is a 프로그래머
print('{} is a {}'.format(name, job))       # 홍길동 is a 프로그래머
print('{1} is a {0}'.format(name, job))     # 프로그래머 is a 홍길동
print('{j} is a {n}'.format(n=name, j=job)) # 프로그래머 is a 홍길동

