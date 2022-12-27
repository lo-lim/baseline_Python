# 재귀함수(Recursive Function)
# : 함수 안에서 자기자신의 함수를 호출하는 함수를 재귀함수라고 한다.

    
def call():                 # 재귀함수
    print('무한출력')
    
    call()                  # 자기자신의 call() 함수 호출
    
    
# 외부에서 call() 함수 호출
call()

#외부에서 call()함수를 호출하면 위에 정의한 call함수의 과정이 실행이 되는데 그 과정안에 자기자신의 call()함수를 또 호출하니까 계속 출력됨.
#어느순간 그 범위를 넘어가면 무한으로 출력하다가 더이상 출력하지 않음.
