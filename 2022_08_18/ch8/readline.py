# data/movie_quotes.text 파일 읽기 : readline()
# readline() : 줄 단위로 텍스트를 읽어오는 역할

# 1. 파일 열기
file = open('../data/movie_quotes.txt', 'r')

# 2. 파일 읽기
line = file.readline()         # 첫번째 라인을 읽어옴
print('line:', line)

# readline()함수는 파일의 끝에 도달하면 ''을 리턴함
while line != '':       #즉 !=를 썼으니 파일의 끝에 도달하지 않는다면, 결국 읽어올 데이터가 있다면이라는 의미
    print(line, end='')
    line = file.readline()

# 3. 파일 닫기
file.close()


#파일 열 떄는 '../상위디렉토리/열 파일 이름'