# data/stockcode.txt 파일을 읽어와서 출력
# read() : 텍스트 파일의 모든 내용을 읽어와서 문자형으로 리턴

with open('../data/stockcode.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)


#with open을 하면 밑에 close함수를 쓰지 않아도 자동으로 닫아줌
#as뒤에 별칭은 임의로 아무거나 써도 가능.
#별칭을 .read()로 읽어와서 data라는 변수에 지정해서 출력하기