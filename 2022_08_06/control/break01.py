# break 문 : 반복문을 빠져 나오는 역할

# 무한루프

i=1
while True:    #조건식히 항상 True가 되기 때문에 무한 출력된다.
     print(i, '무한 출력')
     if i == 100:
          break
         #i가 100이 되었을 때 break가 되어서 출력이 멈춘다는 의미
     i += 1
