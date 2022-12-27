# user 테이블에 데이터 입력    #여기서 입력한 값들이 naverDB에 저장됨

import sqlite3                #잘못된 정보를 갖고 입력을 하면 오류가 발생하기 때문에 try, except 함수를 이용

try:
    # 데이터베이스 접속
    con = sqlite3.connect('naverDB')

    cursor = con.cursor()            #커서를 만들어야함
    
    while True:                                     #while을 통해서 True니까 계속 실행을 하다가 사용자 ID에서 공백을 입력하면 break가 되어서 입력을 멈추게 함
        data1 = input('사용자 ID?')
        if data1 == '':
            break              #사용자 id에서 더 이상 입력하지 않고 공백을 입력하면 멈춘다는 의미
        data2 = input('사용자 이름?')
        data3 = input('사용자 Email?')
        data4 = input('사용자 생년월일?')

        # sql = "insert into user values('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "')"
        sql = "insert into user values(?, ?, ?, ?)"    #컬럼이 id, 이름, email, 생년월일로 4개가 있으니 물음표 4개
        cursor.execute(sql, (data1,data2,data3,data4))   #각각 ?에 사용자가 입력한 값들이 하나하나 순차적으로 적용됨.

    con.commit()

except Exception as err:
    print(err)
    print('데이터 베이스 연결 실패')
finally:
    con.close()






