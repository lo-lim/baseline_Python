# 리스트의 연산 : +, *(반복)

# 리스트의 연산 : +
data1 = ['a','b','c','d','e']     #list를 직접 입력해서 만들기
data2 = ['f','g','h','i','j']
result1 = data1 + data2
result2 = data2 + data1

print('result1:', result1)          # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print('result2:', result2)          # ['f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'e']

#  리스트의 연산 : *
listdata = list(range(3))           # [0, 1, 2]   #range함수를 이용해서 list만들기
print(listdata)

result = listdata * 3               # listdata를 3번 반복한 리스트
print('result:', result)            # [0, 1, 2, 0, 1, 2, 0, 1, 2]

#list에서의 +, *는 리스트 안에 있는 원소들끼리 더해지거나 곱해지는 것