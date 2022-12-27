# pandas로 csv파일 읽기

import pandas as pd

# pandas 모듈을 이용해서 CSV파일을 읽어와서 데이터프레임을 만든다.
df = pd.read_csv('../data/list-utf8.csv', encoding='utf-8')    #..은 내가 불러올 파일 기준 상위 디렉토리에 있다는 내용.  #인코딩을 설정해야 한글이 깨지지 않음
print(type(df))      #실행하면 pandas~~~~~DataFrame으로 출력. 쉽게 말하면 행과 열을 가진 표.  #csv 파일을 불러오면 대부분 표 형식임.
print(df)
#      ID    이름    가격
# 0   1000   비누    300
# 1   1001   장갑    150
# 2   1002   마스크  230

# 컬럼명으로 해당 정보 구하기
print(df['ID'])
print(df['이름'])
print(df['가격'])

#가로로 되어 있는 열은 colum이라고 하고 세로로 되어 있는 행을 index라고 부름