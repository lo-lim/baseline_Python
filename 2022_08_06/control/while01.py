# 반복문 : while문
# while  조건식 :   #이 조건식은 비교 연산자로 이용
#     조건식이 참인 경우에 실행될 문장

# '사랑해요' 메세지를 10번 출력

i = 1                          # 초기값  #반드시 초기값이 할당되어야 한다.
# 1번부터 출력하기 위헤서 i를 1로 지정함.
while i <= 10 :                # 조건식
    print(i,'사랑해요')   #1이 10보다 작은게 True이기 때문에 출력된다.
    # i++                      # 파이썬은 증감 연산자를 지원하지 않는다
    # i = i + 1                #  ++i (x), i++(x)
    i += 1                     # 증감식
#계속 1씩 더해서 값이 출력이 되었는데 11이 되는 순간 위에 10보다 작거나 같다는 조건문에 해당이 안 됨
#따라서 10까지만 출력이 되고 끝남

