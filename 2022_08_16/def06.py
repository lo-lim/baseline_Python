# 입력받은 매개변수에 따라 문자열을 반복 출력하는 함수

def str(text, cnt):
    for i in range(cnt):      # 0 ~ 2까지 3번 루프가 돌아감
        print(text, i+1)

# 함수 호출
str('안녕하세요', 3)
str('파이썬', 5)
str('자바', 3)
str('스프링')                  # 오류 발생 #cnt에 해당하는 값이 없기에 오류가 발생하는 것.

#return을 해도 되고 안 해도 됨. 즉 돌려주지 않고 바로 print로 출력이 가능함
#for는 루프를 돌아가면서 출력하는 거기에 return을 이용해서 하나의 값으로 돌려주기가 힘들기에 바로 print해서 출력하는 것임
# return은 하나의 값을 돌려주는 것. 즉 위에처럼 두 개의 값을 돌려줘야 하는 거는 바로 print을 씀
