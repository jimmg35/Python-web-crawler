import requests
from bs4 import BeautifulSoup

total_date = [] #資料庫用
total_push = []
total_title = []
total_author = []

a = 1 #設定頁數
b = 7976 #最新頁數+1

for times in range(a,b):
    li_date = [] #監看用
    li_push = []
    li_title = []
    li_author = []
    url = "https://www.ptt.cc/bbs/movie/index" + str(times) + ".html"
    r = requests.get(url).content
    soup = BeautifulSoup(r,"html.parser")
    r_ent = soup.findAll("div","r-ent")
    for i in r_ent:
        if i.find("div","nrec").string == None:
            li_push.append("0")
            total_push.append("0")
        else:
            li_push.append(i.find("div","nrec").string)
            total_push.append(i.find("div","nrec").string)
    #print(li_push)
    for j in r_ent:
        if j.find("a") == None:
            li_title.append("文章已被刪除")
            total_title.append("文章已被刪除")
        else:
            li_title.append(j.find("a").string)
            total_title.append(j.find("a").string)
    #print(li_title)
    for k in r_ent:
        li_author.append(k.find("div","author").string)
        li_date.append(k.find("div","date").string)
        total_author.append(k.find("div","author").string)
        total_date.append(k.find("div","date").string)
    #print(li_author)  
    for push,title,author,date in zip(li_push,li_title,li_author,li_date):
        print(f"{push}  {title}")
        print(f"作者:{author}     日期:{date}")
        print("===================================================")
        #f.write(push + "/" + title + "\n")
        #f.write(author + "/" + date + "\n")
        #f.write("--------------------------------------\n")
    #print(type(j.find("a")))
    print(f"第{times}頁資料")

print(f"總共爬取了{b-a}頁的資料")
print(f"含有{len(total_title)}篇文章")

#寫入檔案
f = open("file.txt","a",encoding = "UTF-8")
for push,title,author,date in zip(total_push,total_title,total_author,total_date):
    f.write(f"{push}  {title}\n")
    f.write(f"作者:{author}     日期:{date}\n")
    f.write("===================================================\n")
f.close()