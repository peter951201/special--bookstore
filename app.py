import streamlit as st
import requests

def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' 
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res


def getcountyoption(items):
    optionlist=[]
    for item in items:
        name=item['cityName'][0:3]
        if name not in optionlist:
            optionlist.append(name)
    return optionlist

def getSpecificBookstore(items, county):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        if county in name:
            specificBookstoreList.append(item)
    return specificBookstoreList






def app():
    bookstorelist= getAllBookstore()
    countyoption=getcountyoption(bookstorelist)
	# 呼叫 getSpecificBookstore 並將回傳值賦值給變數 specificBookstore

    st.header('特色書店地圖')
    st.metric('Total bookstore',len(bookstorelist) )
    county = st.selectbox('請選擇縣市',countyoption)
    specificBookstore = getSpecificBookstore(bookstorelist, county)

	# 用 st.write 將目標書店的總數量計算出來，格式：總共有3項結果
    st.write(f'總共有{len(specificBookstore)}項結果')

if __name__ == '__main__':
    app()



