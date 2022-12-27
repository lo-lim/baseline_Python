# 구구단 2~9단 까지 출력하는 프로그램 작성
# 각 단을 열방향으로 출력

for d in range(2,10): #2~9까지 연속으로 출력
    print('[',d,'단]', end='\t\t\t')
print()
for i in range(1, 10): #1~9까지 연속으로 출력
    for dan in range(2, 10):
        print(dan,'*',i,'=',dan*i, end='\t\t')
    print()


# quiz 3 #내가 푼 코딩 식
# for dan in range(2,10):
#     print('[ {0}단 ]' .format(dan), end='\t\t')
# print()
# for i in range(1, 10):
#     for dan in range(2,10):
#         print(dan, '*', i, '=', dan*i, end='\t')
#     print()