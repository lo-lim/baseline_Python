# 반복문 : for문

# for  변수  in  range() :
#    반복 실행할 문장

# 1 ~ 10 까지 합을 구하는 프로그램 작성

sum = 0  #처음으로 할당되는 값인 초기값을 0으로 잡아야 +계산식에 영향을 주지 않음
for i in range(1, 11):              #  1 ~ 10
    sum = sum + i                   # sum += i
    print('1~',i,'=',sum)
# 1=0+1
# 3=1+2
# 6=3+3
#계속 누적되는 방법
print('sum=', sum)


#개어렵다.. 복습 필수... 진짜 코딩은 어렵다 근데 재밌다...

sum=0
for i in range(1,11):
    sum= sum+i
print('sum=' ,sum)