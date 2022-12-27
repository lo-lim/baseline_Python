# pandas로 excel 파일 읽어오기

import pandas as pd

# 엑셀파일 열기
book = pd.read_excel('../data/stats_104102.xlsx',
                     sheet_name='stats_104102',
                     header=1)      # 첫번째 줄을 헤드로 설정
print(book)

# 2015년 인구수로 내림차순 정렬
book = book.sort_values(by=2015, ascending=False)
print(book)

#sort_values 함수를 기준으로 내림차순 정렬 가능, by=2015이라는 것은 2015년을 기준으로 정렬(2015년 기준 서울부터 내림차순), ascending=Fasle라는 것은 기본적인 오름차순이 아니라 내림차순 정렬을 하겠다는 의미