# 딕셔너리의 정렬 : sorted() 함수
# 딕셔너리의 key(아기이름)를 이용해서 오름차순, 내림차순 정렬?
# 딕셔너리의 value(출생아수)를 이용해서 오름차순, 내림차순 정렬?

# { 'key ' : 'value' } = { '아기이름' : 출생아수 }
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245 , 'Michale':27115,
         'Bob':5887, 'Kelly':7855}

#----------------------------------------------------------------------
# 딕셔너리의 key를 리턴하는 함수
def f1(x): #함수를 정의할 때는 def이용,  x라고 된 것은 매개변수, return은 값을 돌려준다는 의미
    return x[0]

# 딕셔너리의 value를 리턴하는 함수
def f2(x):
    return x[1]

#f1은 0의 값 즉 key를 , f2는 1의 값 즉 value값을 할당 받음

# 1. 딕셔너리의 key(아기이름)를 이용해서 오름차순
result1 = sorted(names)
print('result1:', result1)              # ['Aimy', 'Bob', 'Kelly', 'Mary', 'Michale', 'Sams', 'Tom']

result2 = sorted(names.items(), key=f1) #key라는 것이 f1이라는 함수를 받아냄. 즉 names.intems()의 값이 위에 f1함수의 매개변수 x임
#names.items()의 값은 위에 dict안에 있는 key와 value값 둘다인데 return x[0]이니 0번방에 있는 key값
print('result2:', result2)              # [('Aimy', 9778), ('Bob', 5887), ('Kelly', 7855), ('Mary', 10999), ('Michale', 27115), 'Tom']

# 2. 딕셔너리의 key(아기이름)를 이용해서 내림차순
result3 = sorted(names, reverse=True)
print('result3:', result3)              # ['Tom', 'Sams', 'Michale', 'Mary', 'Kelly', 'Bob', 'Aimy']

result4 = sorted(names.items(), reverse=True , key=f1)  #f1인 즉 key 값을 갖고 정렬하라는 의미
print('result4:', result4)              # [('Tom', 20245), ('Sams', 2111), ('Michale', 27115), ('Mary', 10999), ('Kelly', 7855)y']

# 3. 딕셔너리의 value(출생아수)를 이용해서 오름차순
result5 = sorted(names.items(), key=f2) #f2인 즉 value값을 갖고 정렬해라 라는 의미
print('result5:', result5)              # [('Sams', 2111), ('Bob', 5887), ('Kelly', 7855), ('Aimy', 9778), ('Mary', 10999),

# 4. 딕셔너리의 value(출생아수)를 이용해서 내림차순
result6 = sorted(names.items(), reverse=True , key=f2)
print('result6:', result6)              # [('Michale', 27115), ('Tom', 20245), ('Mary', 10999), ('Aimy', 9778), ('Kelly', 7855)