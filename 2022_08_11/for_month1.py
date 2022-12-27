# 1 ~ 12월 중에서 달(Month)에 'r'이 들어있는 달(Month)을 출력

# tuple
months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")


for month in months:
    if 'r' in month.lower(): #.lower는 소문자로 바꿔주는 함수
        print(month)


# for month in months:
#     if month.count('r')>0: #.count 함수는 r의 개수가 1개라도 있으면 해당 월을 출력
#         print(month)

# quiz 1 (내가 제출한 과제)
for i in ['January', "February", "March", "April", 'May', 'June', 'July',
         'August', "September", "October", "November", "December"]:
    if 'r' in i:
        print(i)