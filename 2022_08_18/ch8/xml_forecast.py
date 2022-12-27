# 기상청의 날씨 정보 구하기   #xml은 여러가지 데이터를 저장하기 위한 포맷중의 하나, 웹사이트의 구조로도 가능

from bs4 import BeautifulSoup           # html, xml파일을 분석할때 사용하는 모듈    #bs4라는 라이브러리에 있는 beautifulsoup함수 이용
import urllib.request as req            # 다운로드     #파일을 다운받게 하는 모듈
import os.path

url='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'     #이걸 복붙해서 브라우저에 붙이면 xml파일 형식으로 열려짐

savename = 'forecast.xml'

# if not os.path.exists(savename):      # 현재 디렉토리에 forecast.xml 파일이 없으면
req.urlretrieve(url, savename)          # forecast.xml 파일 다운로드

# BeautifulSoup모듈로 분석하기               #원하는 정보만 선택적으로 뽑아올 때 이용하는 함수
xml = open(savename, 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')   #파일을 open한 것을 xml변수에 저장하고 다시 beautifulsoup함수에 넣어서 soup이라는 변수에 넣기
# print(soup)

# 전국 날씨정보를 info 딕셔너리에 저장                                 #<>가 앞뒤로 있는 값들을 적어줘야함. forecast.xml 파일 참고  #location태그 안에 도시명, 날씨, 기온들이 다 있음. 모든 location이 끝날
#때까지 for함수를 이용해서 루프를 돌린다.
info = {}               # info = { name : weather }
for location in soup.find_all('location'):                       #find_all은 모든 것을 다 불러오는 것이고 find는 ()안에 있는 태그명만 불러옴
    name = location.find('city').text           # 도시명          #.text라는 의미는 안에 들어있는 정보만 뽑는다는 것
    wf = location.find('wf').text               # 날씨
    tmx = location.find('tmx').text             # 최고기온
    tmn = location.find('tmn').text             # 최저기온

    weather = wf + ':' + tmn + '~' + tmx     #도시명이 key인 name, 날씨가 value인 weather #weather이라는 변수에 wf와 tmx,tmn을 +로 연결해서 한개로 묶음

    if name not in info:
        info[name] = []     #만약 name이 info라는 딕셔녀리에 없다면 name의 value값은 공백으로 처리하고 만약 있다면 , ( :에 들여쓰기가 아니기에 위에 조건식에 해당되지 않고) , info[name]즉 value인 weather값이
        # info의 value 값에 추가가 되는 것
    info[name].append(weather)

print(info)

# 각 지역의 날씨를 구분해서 출력
for name in info.keys():     #.keys()는 딕셔너리의 key값만 출력
    print('+', name)                # name : 도시명
    for weather in info[name]:
        print('|', weather)         # weather


