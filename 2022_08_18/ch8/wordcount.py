# 텍스트 파일(data/data.txt)에서 wordcount를 내림차순으로 정렬해서 출력               #ㅈㄵㄵㄵㄴ 어렵다... 복습 왕왕필수 돼지꼬리 용용꼬리 댕댕

# 딕셔너리 = { '단어' : 빈도수 }

# 각 단어의 빈도수를 구해주는 함수
def getTextFreq(filename):    #파일명이 매개변수로 지정됨
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()          # data.txt 파일 전체 내용을 읽어옴   #read함수로 불러옴
        tmp = text.split()       # split()함수로 파싱된 단어들을 리스트로 리턴  #공백을 기준으로 잘라서 list로 리턴하기 위해서 split함수 이용

        fa = {}                  # 비어있는 딕셔너리
        for c in tmp:
            if c in fa:          # 딕셔너리 fa에 key(단어)가 있으면
                fa[c] += 1       # 해당단어의 빈도수를 1증가
            else:                # 딕셔너리 fa에 key(단어)가 없으면
                fa[c] = 1        # 딕셔너리에 빈도수 1 할당(처음나온 단어)  #처음 나왔기 때문에 빈도수를 1로 설정 만약 계속 있으면 위에 if식에 해당되어서 1씩 추가로 늘어남

    return fa                    # 함수를 호출한 곳에 딕셔너리 fa 리턴    #이 값을 함수를 불러낸 식에다가 돌려줌

# result = getTextFreq('../data/data.txt')       #위에 함수를 만들 때 매개변수가 파일명이었으니 여기에 파일명의 위치를 적어줌 #이 식들이 위에 설정한 함수를 호출한 것
# result = getTextFreq('../data/alice.txt')
result = getTextFreq('../data/hong.txt')
print(type(result))              # <class 'dict'>
print(result)

# 단어(key)를 기준으로 오름차순 정렬     #lambda를 굳이 쓰지 않아도 애초에 key값을 기준으로 하긴 함.
print(sorted(result.items()))
print(sorted(result.items(), key=lambda x : x[0]))   #key= lambda x:x[0]이 식의 의미는 key값을 lamba의 x값 즉 result.intmes()인 key, value값에 해당하는데 이것 중에 0번방을 지정한다니까 결국 key값

# 단어(key)를 기준으로 내림차순 정렬
print(sorted(result.items(), key=lambda x : x[0], reverse=True))

# 단어의 빈도수를 기준으로 내림차순 정렬 : 10, 9, 8....
result = sorted(result.items(), key=lambda x : x[1], reverse=True)
print(result)

for c, freq in result:
    print('[%s] - [%d]회' %(c, freq))     #c가 단어인 key, freq가 빈도수인 value에 해당


