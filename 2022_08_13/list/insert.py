# insert() : 리스트의 특정 위치에 원소를 삽입할때 사용되는 함수
# insert( 인덱스 번호, 데이터 )

a = [1, 2, 3]

# 인덱스 0번 위치에 4를 삽입
a.insert(0, 4)
print('a:', a)                  # [4, 1, 2, 3]

# 인덱스 3번 위치에 5를 삽입
a.insert(3, 5)
print('a:', a)                  # [4, 1, 2, 5, 3]


#append 함수는 뒤에 하나씩 추가하는 것이고 insert는 인덱스 번호를 이용해서 원하는 위치에 삽입하는 것