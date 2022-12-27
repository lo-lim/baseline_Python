# 반복문 : for문

# 구구단 2~9단 까지 출력하는 프로그램 작성

for dan in range(2, 10):                    # 2 ~ 9
    # print('[',dan,'단 ]')
    print('[ {}단 ]'.format(dan))
    for i in range(1, 10):                  # 1 ~9
        # print(dan, '*', i, '=', dan*i)
        print('{0} * {1} = {2}'.format(dan, i, dan*i))
    print()

#구구단 세로로 출력
for dan in range(2, 10):
    print('[', dan,'단 ]')
    for i in range(1, 10):
        print('{0} * {1} = {2}' .format(dan, i, dan*i))
    print()


for i in range(1, 10):
    for dan in range(2,10):
        print(dan, '*', i, '=', dan*i, end='\t')
    print()

#구구단 가로로 출력
for dan in range(2,10):
    print('[ {0}단 ]' .format(dan), end='\t\t')
print()
for i in range(1, 10):
    for dan in range(2,10):
        print(dan, '*', i, '=', dan*i, end='\t')
    print()

