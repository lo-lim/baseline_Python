# 반복문 : while문
# while  조건식 :
#     조건식이 참인 경우에 실행될 문장

# 1 ~ 10 까지 합을 구하는 프로그램 작성

i=1; sum=0                      # 초기값   #변수가 2개가 필요함(i, sum)
while i <= 10:                  # 조건식
    sum += i #합을 누적시키기 위한 식, sum=sum+i
    i += 1                      # 증감식 : i=i+1

print('1~10까지 합:', sum)



