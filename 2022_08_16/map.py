# map() 내장함수
# : 인자를 바꾸어가며 함수를 반복 호출하여 결과를 return 받는 함수

def f(x):
    return x*x

li = [1, 2, 3, 4, 5]

# 방법1.
print('1.반복문을 이용한 실행')
for i in li:
    print(f(i), end='\t')
print()

# 방법2.
print('2.map() 함수를 이용한 실행')
result = list(map(f, li))  #li에있는 인수들을 위에 정의내린 f함수에 적용해서 map함수를 이용해서 return된 값을 list로 출력
print('result:', result)

# 방법3.
print('3.map() 함수와 lambda를 이용한 실행')
result2 = list(map(lambda x : x*x, li)) #li에 있는 인수들이 x에 각각 하나씩 적용됨
print('result2:', result2)

