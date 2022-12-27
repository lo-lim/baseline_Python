# pandas로 데이터프레임을 생성하고, 생성된 데이터프레임을 CSV파일에 저장

import pandas as pd

data = [[1,2,3,4],[5,6,7,8]]        # 중첩 리스트   #중첩 리스트를 바탕으로 직접 행과 열을 가진 데이터프레임(표)를 만들 수 있음

# 데이터프레임 생성
df = pd.DataFrame(data)
print(df)
#    0  1  2  3            컬럼번호   #따로 지정을 하지 않으면 0번부터 시작함
# 0  1  2  3  4            인덱스번호 : 0
# 1  5  6  7  8            인덱스번호 : 1

# 데이터프레임을 CSV파일로 저장
df.to_csv('../data/df.csv', header=False, index=False)  #header와 index를 False로 설정했기에 컬럼과 인덱스 번호를 설정하지 않겠다는 의미
print('저장 성공')