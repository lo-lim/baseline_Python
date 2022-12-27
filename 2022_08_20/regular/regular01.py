# 정규표현식을 사용하지 않고 주민번호 뒷자리를 * 로 변경

data = """
        park 800905-1049118
        kim  700905-1059119
       """
result=[]
for line in data.split('\n'):           # line = "park 800905-1049118"           #\n을 기준으로 나눈다는 것은 들여쓰기 한 kim도 같이 불러오겠다는 의미
 word_result=[]                         # word = "park"

 for word in line.split(' '):           # word = "800905-1049118"
    if len(word)==14 and word[:6].isdigit() and word[7:].isdigit():  #길이가 14자리이고 앞에 6자리와 뒤에 6자리가 숫자면 출력하겠다는 의미
        word = word[:6]+'-'+'*******'   # word = "800905-*******"
    word_result.append(word)            # word_result=["park","800905-*******"]
 result.append(" ".join(word_result))
print('\n'.join(result))


#대충 이런 흐름이다 하고 전체적으로 함수 다 복습하고 다시 적용


