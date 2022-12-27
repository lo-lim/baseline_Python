# 키보드로 입력한 내용을 파일로 저장하기 : writelines()
# writelines() : 리스트의 내용을 읽어와서 파일로 저장하는 역할

count = 1
data = []                       #  비어있는 리스트
print('파일에 내용을 저장 하려면, Enter키를 누르세요.')

while True:
    text = input('[%d] 파일에 저장할 내용을 입력하세요?'%count)
    if text == '':              # 아무런 값을 입력하지 않고 Enter키 누르면
        break                  #위에 조건식처럼 아무런 값을 입력하지 않고 Enter를 누르면 braek 즉 멈춤
    data.append(text+'\n')    #\n\으로 인해 줄 바꿈이 적용됨
    count += 1

print(data)

with open('../data/save01.txt', 'w', encoding='utf-8') as file:
    file.writelines(data)


#즉 Enter를 누르지 않고 계속 데이터를 입력하면 break가 걸리지 않고 계속 저 비어있는 리스트 data에 하나하나 추가
#writelines함수를 이용해서 list에 있는 값들을 테스트에 다 추가함.
