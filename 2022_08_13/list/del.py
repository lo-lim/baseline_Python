# del 명령 : 리스트의 특정 원소를 index번호로 삭제하는 명령
# 형식 :  del  리스트[ index 번호 ]

a = [1, 2, 3]
del a[1]                    # 인덱스 1번 원소 삭제
print('a:', a)              # [1, 3]

b = [1, 2, 3, 4, 5]
del b[2:]                   # 인덱스 2번 원소부터 끝까지 삭제
print('b:', b)              # [1, 2]

del b                       # 리스트 b를 메모리 상에서 삭제
print(b)                    # NameError: name 'b' is not defined

#del은 함수가 아니라 명령이기 때문에 괄호 ( 를 쓰지 않음.
#del b를 해서 아예 메모리 상에서 지워서 b is not defined라는 메세지가 뜸

