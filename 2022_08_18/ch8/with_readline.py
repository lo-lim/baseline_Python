# data/stockcode.txt 파일을 읽어와서 출력
# readline() : 텍스트 파일 한줄만 읽어와는 역할

with open('../data/stockcode.txt', 'r', encoding='utf-8') as file:

    line = file.readline()          # 첫번째 줄을 읽어옴

    num = 1  #앞에 번호를 1번부터 시작하기 위해 초기값을 1이라고 지정
    while line != '':
        print('%d %s' %(num, line), end='')
        line = file.readline()
        num += 1

