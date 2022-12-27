# 데이터베이스와 테이블 생성

import sqlite3

# 데이터베이스 생성 함수
def create_table():
   con = sqlite3.connect('naverDB')      # 데이터베이스 생성 및 연결  #sqlite3.connect함수가 데이터베이스를 생성하거나 이미 생성되어 있으면 연결해 주는 함수

   cursor = con.cursor()                 # 커서 생성

   # user 테이블 생성    #.execute함수를 이용해서 user라는 이름의 테이블 생성  #id, username, email, birth을 20자리까지 만들자
   cursor.execute('''create table user(
                       id char(20),
                       username char(20),
                       email char(20),
                       birth char(20) )
                  ''')

   con.commit()
   con.close()

#여기까지의 table user 식의 테이블 생성

if __name__=='__main__':
    create_table()              # 함수 호출






