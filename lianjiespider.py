#_*_ coding:utf-8 _*_
import os
import requests
import time
from  bs4 import BeautifulSoup
def single(url,title):
    # time.sleep(2)
    html=requests.get(url)
    soup=BeautifulSoup(html.text)
    for link in soup.find_all('img'):
        keep(link.get("src"),title)
def keep(url,title):
    try:
        h = requests.get(url)
    except:
        pass
    path=os.path.join(r"C:\Users\asus-pc\Desktop\beautifulgirl\333",title)
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except:
            pass
    name=str(time.time())[-7:-3]
    imgpath=os.path.join(path,name)+".jpg"
    #写入图片
    with open(imgpath, 'wb') as f:
        f.write(h.content)
def frist(firsturl):
    html=requests.get(firsturl)
    soup = BeautifulSoup(html.content)
    for link in soup.find_all('a'):
        href=link.get('href')
        l=os.path.join("https://www.1102f.com/",href[1:])
        title = link.get_text()
        print title
        if len(href) == 19 or len(href) == 15 or len(href) == 16 or len(href) == 17 or len(href) == 18 :
            single(l,title)

if __name__ == "__main__":
    print "anction time :"
    print time.strftime("%Y-%m-%d %H:%M:%S")
    list=[]
    url1=r"https://www.1102d.com/Html/63/index.html"
    list.append(url1)
    for i in range(2,182):
        url=r"https://www.1102d.com/Html/63/index-%d.html"%i
        list.append(url)
    for i in list[::-1]:
        frist(i)
    print "end time:"
    print time.strftime("%Y-%m-%d %H:%M:%S")
# single(r"https://www.1102d.com/Html/63/379.html","test")