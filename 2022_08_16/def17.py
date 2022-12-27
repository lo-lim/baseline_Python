# 중첩함수(Nested Function)
# : 함수 안에 정의된 함수           #함수 안에 함수가 있음

import math

def stddev(*n):                         # 표준편차

    def mean():                         # 평균 : 중첩함수
        return sum(n) / len(n)

    def variance(m):                    # 분산 : 중첩함수
        total = 0
        for i in n:
            total += (i-m)**2
        return total / (len(n)-1)

    v = variance(mean())
    print('분산(v):', v)

    return math.sqrt(v)

print('표준편차', stddev(2.3, 1.7, 1.4, 0.7, 1.9))


#자세히 설명 안 하고 넘어감. 그냥 이런 함수가 있구나 하고 넘기기


