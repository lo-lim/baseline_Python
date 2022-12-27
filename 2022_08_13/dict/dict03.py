# 딕셔너리의 값 수정

# { 'key ' : 'value' } = { '아기이름' : 출생아수 }
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245 , 'Michale':27115,
         'Bob':5887, 'Kelly':7855}

print(names)
print(names['Aimy'])            # 9778  #Aimy의 Key를 바탕으로 Value 값을 구하기
print(names.get('Aimy'))        # 9778  #괄호 (을 사용하기 위해서는 .get을 더 추가함

# 딕셔너리의 값 수정 : Aimy 의 값을 9778에서 10000으로 수정
names['Aimy'] = 10000

print(names['Aimy'])            # 10000

#key 값 자체를 수정하는 것은 어렵지만 key값을 이용해서 value를 수정할 수 있음