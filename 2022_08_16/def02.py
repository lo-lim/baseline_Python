# 매개 변수가 있는 함수
# : 절대값을 구하는 함수

# 사용자 정의 함수
def abs(n):                     # n : 매개변수(parameter)
    if n < 0:
        n = -n
    return n                    # return문 : 함수를 호출한 곳에 값을 돌려주는 역할

# 함수 호출
abs(-30)
print('돌려 받은값1:', abs(-30))   #위에서 return한 n값을 abs(-30)에 돌려줌

result = abs(-50)
print('돌려 받은값2:', result)

#abs함수는 절댓값(양수)를 만들어줌
#return 구문은 돌려줄 값이 없으면 안 써도 됨. return 구문은 함수를 쓸 때 가장 마지막 줄에 써야 함
#매개변수가 없으면 abs() 이런식으로 함수만 불러서 호출할 수 있지만 매개변수가 있으면 이 변수를 먼저 불러야함 이후 print로 출력
#호출한 값을 바로 print하거나 새로운 변수에 지정해서 그 변수를 print로 호출하는 방법이 있음