# 반복문 : for문
# for  변수  in  컬렉션:

# 리스트(list)
list = ['사과','딸기','포도','배','키위','바나나']
print(type(list))              # <class 'list'>
print(list)                    # ['사과', '딸기', '포도', '배', '키위', '바나나']
print(list[0])                 # 사과

for i in list:  #list 안에 있는 값들이 다 끝날때까지 반복해서 출력
    print(i, end=' ')           # 사과 딸기 포도 배 키위 바나
                                # end=' ' 에서 ' 사이에 공백 만큼 값이 벌어져 출력
print()

# 튜플(tuple)
t = ('red','orange','yellow','green','blue','navy','purlpe')
print(type(t))                  # <class 'tuple'>
print(t)                        # ('red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purlpe')
print(t[0])                     # red

for i in t:
    print(i, end=' ')           # red orange yellow green blue navy purlpe
print()

# 딕셔너리(dictionary) : { 'key' : 'value' }
dic = {'애플' : 'http://www.apple.com',
       '구글' : 'http://www.google.com',
       '네이버' : 'http://www.naver.com'}

print(type(dic))                # <class 'dict'>
print(dic)                      # {'애플': 'http://www.apple.com', '구글': 'http://www.google.com', '네이버': 'http://www.naver.com'}
print(dic['애플'])               # http://www.apple.com

for k, v in dic.items():
    print(k,':', v)
#dic는 다른 자료구조와 다르게 key와 value를 둘 다 인식 가능함
#dic.intems()는 k와 v를 한꺼번에 불러오게 하는 함수. 즉  for in 안에 들어 있는 변수명도 두 개로 지정







