# 텍스트 파일(data/data.txt)에 키보드로 입력한 단어의 갯수 구하기


# 키보드로 입력한 단어의 빈도수를 구해주는 함수
def countWord(filename, word):
    with open(filename, 'r') as f:
        text = f.read()     #read함수로 파일 전체를 다 불러옴
        text = text.lower()         # 소문자로 변환

        list = text.split()         # split()함수로 공백으로 파싱된 단어를 리스트로 리턴
        count = list.count(word)    # count()함수로 찾을 단어의 빈도를 구함

    return count

word = input('찾을 단어를 입력 하세요?')
word = word.lower()

# result = countWord('../data/data.txt', word)              #위에 return으로 돌려주는 count값이 함수를 호출한 이 식들에게 돌려줌 즉 count의 값이 result의 값으로 돌려줌
result = countWord('../data/alice.txt', word)
print('[%s]의 갯수: %d회'%(word, result))