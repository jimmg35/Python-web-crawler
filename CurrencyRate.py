import requests
from bs4 import BeautifulSoup

currency_name = [] #髒髒貨幣字串
currency_name_clean = [] #乾淨貨幣字串
currency_dirty = [] #髒髒貨幣價格
currency_clean = [] #乾淨貨幣價格
price_in = []
price_out = []

r = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW").content
soup = BeautifulSoup(r,"html.parser")
table = soup.find("table")
tbody = table.find("tbody")
tr_list = tbody.findAll("tr")
#print(tr_list)

#貨幣名稱
for i in tr_list:
    currency_name.append(i.find("div","visible-phone print_hide").string)
for i in currency_name:
    currency_name_clean.append(i.strip("\r\n "))

#[ [] , [] , [] , [] ]
#買進價格
for j in tr_list:
    currency_dirty.append(j.findAll("td","rate-content-cash text-right print_hide"))
for j in currency_dirty:
    for k in j:
        currency_clean.append(k.string)
#print(currency_clean)

for i in range(0,38,2):
    price_in.append(currency_clean[i])
for i in range(1,38,2):
    price_out.append(currency_clean[i])

f = open("CR.txt","a",encoding = "UTF-8")
for name,InPrice,OutPrice in zip(currency_name_clean,price_in,price_out):
    print(f"{name}  買進:{InPrice}  賣出:{OutPrice}")
    f.write(str(name) + "   買進:" + str(InPrice) + "   賣出:" + str(OutPrice) + "\n")
    f.write("==========================================\n")
f.close()
input()