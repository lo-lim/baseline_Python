# 파일 생성(파일 쓰기) : write()

# 1. 쓰기 모드로 열기
file = open('../data/text.txt', 'w', encoding='utf-8')

# 2. 파일 쓰기(저장)
file.write('안녕\n반갑습니다.\n')
print('저장 성공')

# 3. 파일 닫기
file.close()


#저장할 때는 w쓰기
#\n은 줄 바꾸기
#open으로 열먼 반드시 마지막에 close로 닫아주기
#close를 쓰는 이유는 파일이 잘 생성이 되어도 내용이 저장이 안 되는 경우가 있기에