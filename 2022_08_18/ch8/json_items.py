# data/item.json 파일 읽어오기             #파일을 열어보면 처음 앞뒤는 [ 대괄호가로 되어있고 중간중간에 {로 되어있음 #즉 list 안에 dic가 들어있는 형태

import json

# json 파일 읽어오기
items = json.load(open('../data/item.json', 'r', encoding='utf-8'))          #open한 파일을 저장하기 위해서는 json.load함수 이용 #인코딩을 해 주어야 한글이 깨지지 않음
#만약 파일 자체가 ansl 종류로 저장이 된다면 encoding=utf-8로 해줌.
print(type(items))              # <class 'list'>
print(items)                    # [{'id': '1', 'name': '레몬', 'price': ' 3000',               #1~풍부하다 까지의 한 묶음이 리스트 안에서 0번방에 있음. #id, name, price 등등이 key가 되고 1, 레몬, 3000 등등이 value가 된다.

for item in items:
    print(item['id']+'-'+item['name']+'-'+item['price']+'-'+item['description'])

