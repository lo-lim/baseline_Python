# 문자 변경 : pithon -> python

s = 'pithon'
print(s[1])                       # i

# i -> y 변경
# s[1] = 'y'                      # 오류발생

s = s[:1] + 'y' + s[2:]           # python
print(s)

#문자열에 해당하는 변수들은 다른 변수들로 변경하는 것이 불가능하기에 다른 방법으로 할당, 즉 인덱싱 방법으로 변경