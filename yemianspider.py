#_*_ coding:utf-8 _*_
import os
import requests
import time
from  bs4 import BeautifulSoup
def single(url,title):
    time.sleep(2)
    html=requests.get(url)
    soup=BeautifulSoup(html.text)
    for link in soup.find_all('img'):
        keep(link.get("src"),title)
def keep(url,title):
    h = requests.get(url)
    path=os.path.join(r"C:\Users\asus-pc\Desktop\beautifulgirl\555",title)
    if not os.path.exists(path):
        os.mkdir(path)

    name=str(time.time())[-7:-3]
    imgpath=os.path.join(path,name)+".jpg"
    #写入图片
    with open(imgpath, 'wb') as f:
        f.write(h.content)
def frist(firsturl):
    html=requests.get(firsturl)
    #soup=BeautifulSoup(html.text)
    soup = BeautifulSoup(html.content)
    try :
        topurl = soup.find(attrs={'class': 'next pagegbk'})["href"]
    except TypeError:
        return 0
    for link in soup.find_all('a'):
        href=link.get('href')
        l=os.path.join("https://www.1102f.com/",href[1:])
        #title=link.get_text().encode("utf-8")
        title = link.get_text()
        print title
        if len(href) == 19:
            single(l,title)
            #print keep(href,title)
    # topurl = soup.find(attrs={'class': 'next pagegbk'})["href"]
    return os.path.join("https://www.1102f.com/",topurl[1:])


if __name__ == "__main__":
    print "anction time :"
    print time.strftime("%Y-%m-%d %H:%M:%S")
    url = r"https://www.1102f.com/Html/63/"
    topurl = frist(url)
    while 1:
        time.sleep(3)
        if topurl!=0:
            topurl=frist(topurl)
        else:
            print "end time:"
            print time.strftime("%Y-%m-%d %H:%M:%S")
