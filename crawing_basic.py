
# %%
import json
import csv
# import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

# %%
response = requests.get("http://paullab.synology.me/stock.html")
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# %%
print(soup.select('#update')[0].text)
print("")
print("--------------------")
oneStep = soup.select('.main')[2]
twoStep = oneStep.select('tbody > tr')[1:]
print(twoStep[0])
print("--------------------")
print(twoStep[0].select('td')[0])
print(twoStep[0].select('td')[0].text)
print("--------------------")
print(twoStep[0].select('td')[1])
print(twoStep[0].select('td')[1].text.replace(',', ''))
print("--------------------")

날짜 = []
종가 = []
전일비 = []
거래량 = []

for i in twoStep:
    날짜.append(i.select('td')[0].text)
    종가.append(int(i.select('td')[1].text.replace(",", '')))
    전일비.append(int(i.select('td')[2].text.replace(",", '')))
    거래량.append(int(i.select('td')[6].text.replace(",", '')))

print(날짜, 종가, 전일비, 거래량)

# # %%
# plt.plot(날짜, 종가)
# plt.xticks(rotation=-45)
# plt.show()


# %%
I = []

for i in range(len(날짜)):
    I.append({
        '날짜': 날짜[i],
        '종가': 종가[i],
        '전일비': 전일비[i],
        '거래량': 거래량[i]
    })
print(I)

# %%
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
    json.dump(I, f_write, ensure_ascii=False, indent=4)

# %%
data = ""
with open('data.js', "r", encoding="UTF-8-sig") as f:
    line = f.readline()
    while line:
        data += line
        line = f.readline()

final_data = f"var data ={data};"
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
    f_write.write(final_data)
