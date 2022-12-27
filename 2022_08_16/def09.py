# 가변 매개변수(Arbitary Argument Variable)
# 1. 매개변수 앞에 ** 를 붙이면 가변 매개 변수가 된다.
# 2. 가변 매개변수는 입력 갯수가 달라져도 모두 받을 수 있다.
# 3. **가 붙은 가변 매개변수는 입력받은 값들을 딕셔너리(dict)로 처리한다.

# 가변 매개변수를 가진 함수 정의
def print_team(**players):
    print(type(players))                        # dict

    for k in players.keys():   #dict의 값들 중에서(key, value) key값만 불러오기
        print('{0} = {1}'.format(k, players[k]))

# 함수 호출
print_team(카시야스='GK', 호날두='FW', 알론소='MF', 페페='DF')

#players[k]의 값은 key값의 해당하는 value값이다. 즉 player[페페]=='DF'
