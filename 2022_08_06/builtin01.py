#  내장 함수

# 최대값 : max()
print(max(10, 20))                  # 20
print(max(10, 20, 30, 40, 50))      # 50
print(max([10, 20, 30, 40, 50]))    # 50
print(min('hello world'))           # w (가장 z에 가까운 값을 가장 크다고 정의)
print(min('apple'))
# 최소값 : min()
print(min(10, 20, 30, 40, 50))      # 10
print(min([10, 20, 30]))            # 10

# range() 함수  #주로 for 반복문과 잘 사용됨,
# range(초기값, 최종값, 증감값) : 초기값 ~ 최종값-1 까지 증감
# range(초기값, 최종값) : 초기값 ~ 최종값-1 까지  1씩 증가
# range(최종값) : 0 ~ 최종값-1 까지  1씩 증가
print(range(10))              # range(0, 10)

print(list(range(10)))        # 0 ~ 9  : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10)))      # 1 ~ 9  : [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10,2)))    # [1, 3, 5, 7, 9]
#list는 직접 [ 안에다가 넣는 방법과 range 함수를 이용하는 방법이 있다.
#range는 단독으로 쓰는 것은 큰 의미가 없고 다른 함수와 결합해서 주로 사용.


for i in range(1, 11):        # 1 ~ 10
 print(i) #1부터 10까지의 결과를 세로로 나열


for i in range(10):           # 0 ~ 9
    print(i, end=' ') #0부터 9가지 가로로 나열
print() #print를 한 번 해 주어야 밑에 있는 코딩과 같이 가로로 나열이 안 됨
#즉 print는 줄을 바꿔줄 때 사용하는 것

for i in range(10, 1, -1):    # 10 ~ 2까지 1씩 감소
#10이 초기값이고 최종값이 1이니까 10부터 시작해서 1+1인 2까지 감소
#초기값부터 최종값까지 감소하는 것은 증가하는 것과 반대로 적용
    print(i)

for i in range(10, 1, -2): #10, 8, 6, 4, 2
    print(i)